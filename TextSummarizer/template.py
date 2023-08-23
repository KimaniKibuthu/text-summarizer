"""
Example way to create a template for a project.
"""

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

list_files = [
    "Text Summarizer/.github/workflows/.gitkeep",
    f"Text Summarizer/src/__init__.py",
    f"Text Summarizer/src/components/__init__.py",
    f"Text Summarizer/src/utils/__init__.py",
    f"Text Summarizer/src/utils/common.py",
    f"Text Summarizer/src/logging/__init__.py",
    f"Text Summarizer/src/config/__init__.py",
    f"Text Summarizer/src/config/config.py",
    f"Text Summarizer/src/pipeline/__init__.py",
    f"Text Summarizer/src/entity/__init__.py",
    f"Text Summarizer/src/constants/__init__.py",
    "Text Summarizer/config/config.yaml",
    "Text Summarizer/params.yaml",
    "Text Summarizer/app.py",
    "Text Summarizer/main.py",
    "Text Summarizer/Dockerfile",
    "Text Summarizer/requirements.txt",
    "Text Summarizer/setup.py",
    "Text Summarizer/research/text-summarization.ipynb",
]

for filepath in list_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            logging.info(f"Created file: {filepath}")
    
    else:
        logging.info(f"File already exists: {filepath}")