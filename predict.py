"""
Flower Classifier Predictor
This module provides functions to predict flower classes from images.
"""

import argparse
import json
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image


def process_image(image):
    """
    Preprocesses an image for the model.

    Parameters:
    - image: Raw image data.

    Returns:
    - Processed image suitable for the model.
    """
    image = tf.convert_to_tensor(image, dtype=tf.float32)
    image = tf.image.resize(image, (224, 224))
    image /= 255
    return image.numpy()


def predict(image_path, model, top_k):
    """
    Predict the class of an image.

    Parameters:
    - image_path: Path to the image.
    - model: Trained model to use for prediction.
    - top_k: Number of top predictions to return.

    Returns:
    - Top probabilities and corresponding classes.
    """
    image = Image.open(image_path)
    image_np = np.asarray(image)
    processed_image = process_image(image_np)
    expanded_image = np.expand_dims(processed_image, axis=0)

    probabilities = model.predict(expanded_image)
    top_probs, top_labels = tf.math.top_k(probabilities, k=top_k)

    return top_probs.numpy()[0], top_labels.numpy()[0]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Flower Classifier Predictor')
    parser.add_argument(
        'image_path',
        action="store",
        type=str,
        help='Path to input image.')
    parser.add_argument('model', action="store", type=str,
                        help='Path to saved Keras model.')
    parser.add_argument(
        '--top_k',
        action="store",
        type=int,
        default=5,
        help='Return top K predictions.')
    parser.add_argument(
        '--category_names',
        action="store",
        default='label_map.json',
        help='Path to JSON file for mapping of labels to flower names.')

    results = parser.parse_args()

    print("Parameters:")
    print("image_path: ", results.image_path)
    print("Model: ", results.model)
    print("Top K: ", results.top_k)
    print("Category Names: ", results.category_names)

    print("Loading model...")
    loaded_model = tf.keras.models.load_model(
        results.model,
        custom_objects={'KerasLayer': hub.KerasLayer}
    )

    print("..........................................")
    print("Summary of loaded model:")
    loaded_model.summary()
    print("..........................................")

    probs, classes = predict(results.image_path, loaded_model, results.top_k)

    # Specified encoding for open
    with open(results.category_names, 'r', encoding='utf-8') as f:
        class_names = json.load(f)
    classes = [class_names[str(c + 1)] for c in classes]

    print("Probabilities:", [round(p, 6) for p in probs])
    print("Classes:", classes)
