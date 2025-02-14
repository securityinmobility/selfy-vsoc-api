#!/usr/bin/env python3
# GNU Lesser General Public License v3.0 or later
# @author Dominik Bayerl <dominik.bayerl@carissma.eu>
import re

import torch
import transformers
from torch import Tensor
from transformers import AutoModel, Pipeline, pipeline
from transformers.pipelines import PIPELINE_REGISTRY
from transformers.utils import logging

logging.set_verbosity_info()
logger = logging.get_logger("transformers")


class BinaryEmbedding(Pipeline):
    def _sanitize_parameters(self, **kwargs):
        return {}, {}, {}

    def rebase(self, asm_dict):
        # 're' caches compiled expressions
        loc_pattern = re.compile(r" (loc_|locret_|0x)(\w+)")
        self_pattern = re.compile(r"\$\+(\w+)")

        index = 1
        rebase_assembly = {}

        addrs = list(sorted(list(asm_dict.keys())))

        for addr in addrs:
            inst = asm_dict[addr]
            if inst.startswith("j"):
                loc = loc_pattern.findall(inst)
                for prefix, target_addr in loc:
                    try:
                        target_instr_idx = addrs.index(int(target_addr, 16)) + 1
                    except Exception:
                        continue
                    asm_dict[addr] = asm_dict[addr].replace(
                        f" {prefix}{target_addr}", f" INSTR{target_instr_idx}"
                    )
                self_m = self_pattern.findall(inst)
                for offset in self_m:
                    target_instr_addr = addr + int(offset, 16)
                    try:
                        target_instr_idx = addrs.index(target_instr_addr)
                        asm_dict[addr] = asm_dict[addr].replace(
                            f"$+{offset}", f"INSTR{target_instr_idx}"
                        )
                    except:
                        continue
            rebase_assembly[str(index)] = asm_dict[addr]
            index += 1

        return rebase_assembly

    def preprocess(self, inputs):
        logger.debug(f"Tokenizing function {inputs['name']}")
        asm_dict = self.rebase(inputs["instructions"])
        return self.tokenizer(
            [asm_dict], padding=True, return_tensors=self.framework
        ).to(self.device)

    def _forward(self, model_inputs):
        logger.debug(f"Embedding {len(model_inputs['input_ids'][0])} tokens")
        outputs = self.model(**model_inputs)
        return outputs

    def postprocess(self, model_outputs: Tensor):
        return model_outputs.squeeze()


PIPELINE_REGISTRY.register_pipeline(
    "binary-function-recognition",
    pipeline_class=BinaryEmbedding,
    pt_model=AutoModel,
    default={"pt": ("autobert", "041d4454")},
)
