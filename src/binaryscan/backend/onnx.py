#!/usr/bin/env python3
# GNU Lesser General Public License v3.0 or later
# @author Dominik Bayerl <dominik.bayerl@carissma.eu>

import numpy as np
from typing import List, Dict
from transformers import AutoTokenizer, pipeline
from optimum.onnxruntime import ORTModelForFeatureExtraction
from chromadb.api.types import (
    EmbeddingFunction,
    Embeddings,
)


class ONNX_Runtime(EmbeddingFunction):
    """A class for generating embeddings using ONNX Runtime for feature extraction.

    Attributes:
        model (ORTModelForFeatureExtraction): The ONNX Runtime model for feature extraction.
        tokenizer (AutoTokenizer): The tokenizer for the model.
        pipeline (pipeline): The transformers pipeline for generating embeddings.
    """

    def __init__(
        self,
        model_path: str,
        batch_size: int = 32,
        model_kwargs: dict = {},
        tokenizer_kwargs: dict = {},
    ):
        """Initialize the embedding function."""
        self.model = ORTModelForFeatureExtraction.from_pretrained(
            model_path, **model_kwargs
        )
        self.tokenizer = AutoTokenizer.from_pretrained(model_path, **tokenizer_kwargs)
        self.pipeline = pipeline(
            "feature-extraction", model=self.model, tokenizer=self.tokenizer
        )
        self.batch_size = batch_size

    def __call__(self, input: List[Dict]) -> Embeddings:
        """Run feature-extraction pipeline on input documents."""
        return np.vstack(self.pipeline(input))
