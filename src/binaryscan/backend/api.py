#!/usr/bin/env python3
# GNU Lesser General Public License v3.0 or later
# @author Dominik Bayerl <dominik.bayerl@carissma.eu>

from chromadb.api.types import EmbeddingFunction, Documents, Embeddings
from chromadb.utils.embedding_functions import EmbeddingFunction
from typing import List, Dict
import numpy as np
import requests


class API(EmbeddingFunction):
    """
    API class that inherits from EmbeddingFunction.
    This class serves as a placeholder for API-related functionality that involves
    embedding operations. Currently, it does not implement any methods or attributes.
    Inheritance:
        EmbeddingFunction: Base class for embedding-related functions.
    """

    def __init__(self, api_base: str, model_name: str, batch_size: int = 32):
        """
        Initialize the API class with the base URL of the API and the model name.

        Args:
            api_base (str): The base URL of the API.
            model_name (str): The name of the model to use for embeddings.
        """
        self.api_base = api_base
        self.model_name = model_name
        self.batch_size = batch_size

    def __call__(self, input: List[Dict]) -> Embeddings:
        """
        Send a request to the API to get embeddings for the input data.

        Args:
            input (List[Dict]): A list of dictionaries containing the input data.
            batch_size (int): The size of each batch for processing.

        Returns:
            Embeddings: A numpy array of embeddings.
        """
        all_embeddings = []

        for i in range(0, len(input), self.batch_size):
            batch_input = input[i:i + self.batch_size]
            response = requests.post(
                self.api_base,
                json={"input": batch_input, "model": self.model_name, "encoding_format": "float"},
            )

            # Check if the request was successful
            if response.status_code != 200:
                raise ValueError(f"Request failed with status code {response.status_code}")

            response_data = response.json()

            # Validate the received JSON schema
            if "data" not in response_data or not isinstance(response_data["data"], list):
                raise ValueError("Invalid response format: 'data' key not found or is not a list")

            # Extract embeddings and sort by index
            batch_embeddings = sorted(response_data["data"], key=lambda x: x["index"])
            embeddings = np.vstack([item["embedding"] for item in batch_embeddings])
            all_embeddings.append(embeddings)

        return np.vstack(all_embeddings)
