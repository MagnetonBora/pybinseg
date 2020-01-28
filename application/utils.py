import json
from tensorflow import keras
import efficientnet.tfkeras


def load_model(config_path: str, weights_path: str) -> 'keras.Model':
    with open(config_path, 'r') as f:
        config = json.load(f)
        model = keras.models.model_from_config(config)
        model.load_weights(weights_path)
        return model

