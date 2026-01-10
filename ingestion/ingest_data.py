"""
Data Ingestion Module
Handles data collection and initial loading into the raw data directory.
"""

import os
import shutil
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(
    filename="logs/ingestion.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

SOURCE_PATH = "data/source"
RAW_PATH = "data/raw"

def ingest():
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        target_path = os.path.join(RAW_PATH, timestamp)

        os.makedirs(target_path, exist_ok=True)

        for file_name in os.listdir(SOURCE_PATH):
            # Skip hidden files like .DS_Store
            if file_name.startswith('.'):
                continue
                
            source_file = os.path.join(SOURCE_PATH, file_name)
            target_file = os.path.join(target_path, file_name)

            # Handle both files and directories
            if os.path.isdir(source_file):
                shutil.copytree(source_file, target_file)
            else:
                shutil.copy(source_file, target_file)
            logging.info(f"Successfully ingested {file_name}")

        print("Ingestion completed successfully.")

    except Exception as e:
        logging.error(f"Ingestion failed: {str(e)}")
        print("Ingestion failed. Check logs.")

if __name__ == "__main__":
    ingest()

