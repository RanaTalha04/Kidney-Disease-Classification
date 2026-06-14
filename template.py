import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "kidney"

list_of_files = [
    # GitHub Actions
    ".github/workflows/ci-cd.yml",

    # Config
    "config/config.yaml",
    "params.yaml",

    # Data directories
    "data/raw/",
    "data/processed/train/",
    "data/processed/val/",
    "data/processed/test/",

    # Models
    "models/",

    # Notebooks
    "notebooks/01_eda.ipynb",
    "notebooks/02_custom_cnn.ipynb",
    "notebooks/03_efficientnet.ipynb",

    # Source - root
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/config.py",

    # Source - constants
    f"src/{project_name}/constants/__init__.py",

    # Source - entity
    f"src/{project_name}/entity/__init__.py",

    # Source - config
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/config/__init__.py",

    # Source - components
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/custom_cnn.py",
    f"src/{project_name}/components/efficientnet.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_evaluation.py",

    # Source - pipeline
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",

    # Source - utils
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/utils/gradcam.py",

    # App
    "app/main.py",
    "app/templates/index.html",
    "app/templates/result.html",
    "app/static/styles.css",

    # Tests
    "tests/__init__.py",
    "tests/test_data_ingestion.py",
    "tests/test_model.py",
    "tests/test_api.py",

    # Root config files
    "Dockerfile",
    ".dockerignore",
    ".gitignore",
    "pyproject.toml",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")