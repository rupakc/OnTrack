from utils import classificationutils, featureutils
from config import constants
import numpy as np


def get_delay_in_minutes(feature_dictionary):
    delay_model = classificationutils.load_model(constants.delay_model_file_path)
    featureutils.encode_categorical_values(feature_dictionary)
    feature_array = featureutils.get_feature_list(feature_dictionary)
    return delay_model.predict(feature_array.reshape(1, -1))[0]
