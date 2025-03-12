import logging
from ast import literal_eval
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def read_dataset(file_path: Path) -> pd.DataFrame:
    """Reads a dataset from a CSV file and processes the embedding column.

    Parameters
    ----------
    file_path : str
        The path to the CSV file containing the dataset.

    Returns
    -------
    pd.DataFrame
        A pandas DataFrame containing the dataset with the embedding column
        converted from a string to a list of floats.
    """
    logging.info(f"Reading dataset from CSV file")
    df = pd.read_csv(file_path)
    # Convert the embedding column from string to list of floats
    df["embedding"] = df["embedding"].apply(literal_eval)
    return df


def similar_articles(
    url: str, df_articles: pd.DataFrame, top_n: int = 10
) -> list[list[str, float]]:
    """Finds the top N similar articles based on their embeddings.

    Parameters
    ----------
    url : str
        The URL of the article to find similarities for.
    df_articles : pd.DataFrame
        A DataFrame containing articles with their URLs and embeddings.
    top_n : int, optional
        The number of top similar articles to return, by default 10

    Returns
    -------
    list[list[str, float]]
        A list of lists, where each sublist contains the URL of a similar article and its similarity score.

    Raises
    ------
    ValueError
        If the given URL is not found in the dataset.
    """
    logging.info(f"Finding similar articles for URL: '{url}'")
    if url not in df_articles["url"].values:
        logging.error(f"URL '{url}' not found in the dataset.")
        raise ValueError(f"URL not found in the dataset.")

    current_embedding = df_articles[df_articles["url"] == url]["embedding"].values[0]
    df_search = df_articles[df_articles["url"] != url]
    embeddings = np.vstack(df_search["embedding"].values)
    similarities = cosine_similarity([current_embedding], embeddings)[0]
    # Sort the similarities in descending order (minus sign)
    similar_indices = np.argsort(-similarities)[:top_n]
    return [
        [df_search["url"].iloc[idx], float(similarities[idx])]
        for idx in similar_indices
    ]
