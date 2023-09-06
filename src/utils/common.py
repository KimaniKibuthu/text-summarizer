"""
Module containing the utility files for the project.
"""

import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from box.exceptions import BoxValueError
import yaml
from loging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path    
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Function to read a yaml file and return a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the yaml file.

    Raises:
        BoxValueError: If the yaml file is empty.

    Returns:
        ConfigBox: ConfigBox object.
    """
    try:
        with open(path_to_yaml, "r") as f:
            config = yaml.safe_load(f)
            config = ConfigBox(config)
            logger.info(f"Successfully read yaml file from {path_to_yaml}")
            return config

    except BoxValueError:
        logger.error(f"Yaml file at {path_to_yaml} is empty.")


@ensure_annotations
def  create_directories(path_to_directories: list, verbose=True):
    """
    Function to create directories.

    Args:
        path_to_directories (list): List of paths to the directories.
        verbose (bool, optional): Whether to print out the directories created. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Function to get the size of a file or directory.

    Args:
        path (Path): Path to the file or directory.

    Returns:
        str: Size of the file or directory.
    """
    size = os.path.getsize(path)/1024
    return f"{size} KB" if size < 1024 else f"{size/1024} MB" if size < 1024**2 else f"{size/(1024**2)} GB"


if __name__ == "__main__":
    pass