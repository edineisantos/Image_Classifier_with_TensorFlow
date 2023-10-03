"""
Flower Classifier Predictor Tester

This script tests the predictions made by the model in `predict.py`
on multiple flower images and logs the results.

Author: Edinei Santos
Date: 2023-10-03
"""

import subprocess
import logging

# Setting up the logging configuration
logging.basicConfig(
    filename='./logs/predict_test.log',
    level=logging.INFO,
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

IMAGES = [
    "./test_images/cautleya_spicata.jpg",
    "./test_images/hard-leaved_pocket_orchid.jpg",
    "./test_images/orange_dahlia.jpg",
    "./test_images/wild_pansy.jpg"
]

MODEL_PATH = "image_classifier_model.h5"
LABEL_MAP = "label_map.json"


def test_predict(image_path, model_path, label_map):
    """
    Test prediction on an image and log the results.

    Parameters:
    - image_path: Path to the image.
    - model_path: Path to the saved model.
    - label_map: Path to the JSON file for mapping of labels to flower names.

    Returns:
    None
    """
    command = [
        "python",
        "predict.py",
        image_path,
        model_path,
        "--category_names",
        label_map
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True)
        logging.info("Testing image: %s", image_path)
        logging.info("%s", result.stdout)
    except subprocess.CalledProcessError as e:
        logging.error("Command '%s' returned non-zero exit status %d.\n%s",
                      ' '.join(command), e.returncode, e.output)

    if result.stderr:
        logging.error("%s", result.stderr)


def main():
    """
    Run the tests for predictions on multiple images.

    Parameters:
    None

    Returns:
    None
    """
    for image in IMAGES:
        test_predict(image, MODEL_PATH, LABEL_MAP)


if __name__ == "__main__":
    main()
