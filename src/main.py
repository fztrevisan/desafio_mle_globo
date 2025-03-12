import logging
import sys
from pathlib import Path

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from recomend_articles import read_dataset, similar_articles

CURRENT_DIR = Path(__file__).resolve().parent
DATA_DIR = CURRENT_DIR.joinpath("data")
# colaborador@N093387 desafio_mle_globo % python -m venv .venv
# colaborador@N093387 desafio_mle_globo % source .venv/bin/activate
# (.venv) colaborador@N093387 desafio_mle_globo % pip install -r requirements.txt 
# Set up logging to log to both console and file
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s][%(levelname)s][%(module)s][%(funcName)s]: %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(filename="similarities.log"),
    ],
)

if __name__ == "__main__":
    # Run similar_articles function for all articles in the dataset
    # and save the results to a CSV file
    logging.info("Starting the recommendation process")
    input_file_path = DATA_DIR.joinpath("dataset_rec.csv")
    df_articles = read_dataset(input_file_path)

    recommendations = []
    for row in df_articles.itertuples(index=False):
        recommended_urls = similar_articles(
            url=row.url, df_articles=df_articles, top_n=10
        )
        recommendations.append(
            {
                "url": row.url,
                "recommended_urls": recommended_urls,
            }
        )

    logging.info("Saving results to CSV file")
    output_file_path = DATA_DIR.joinpath("recommendations.csv")
    df_output = pd.DataFrame(recommendations)
    df_output.to_csv(output_file_path, index=False)
    logging.info(f"Recommendations saved to {output_file_path}")
