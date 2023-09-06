import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from dataclasses import dataclass
from pathlib import Path
from loging import logger
from utils.common import get_size
from entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        logger.info("Downloading data...")
        os.system(f"wget {self.config.source_URL} -O {self.config.local_data_file}")
        logger.info(f"Data downloaded at {self.config.local_data_file}")

    def unzip_data(self):
        logger.info("Unzipping data...")
        
        # Detect file extension
        file_ext = os.path.splitext(self.config.local_data_file)[1]
        
        if file_ext == ".zip":
            os.system(f"unzip {self.config.local_data_file} -d {self.config.unzip_dir}")
        elif file_ext == ".rar":
            os.system(f"unrar x {self.config.local_data_file} {self.config.unzip_dir}")
        elif file_ext in [".7z", ".7zr"]:
            os.system(f"7z x {self.config.local_data_file} -o{self.config.unzip_dir}")
        else:
            logger.error(f"Unsupported file format: {file_ext}")
            return

        logger.info(f"Data unzipped at {self.config.unzip_dir}")

    def get_data_size(self):
        logger.info("Getting data size...")
        size = get_size(self.config.unzip_dir)
        logger.info(f"Data size: {size}")

    def run(self):
        self.download_data()
        self.unzip_data()
        self.get_data_size()