from config import constants
from explain import lime_explainer
from utils import classificationutils


def get_explanation_for_instance(single_instance_list):
    delay_model = classificationutils.load_model(constants.delay_model_file_path)
    return lime_explainer.get_explanation_html(single_instance_list,delay_model,constants.NUM_FEATURES,constants.lime_explainer_file_path)


def get_explanation_to_file(single_instance_list, date, from_station, to_station, train_num):
    delay_model = classificationutils.load_model(constants.delay_model_file_path)
    return lime_explainer.write_explanation_to_file(single_instance_list, delay_model, constants.NUM_FEATURES,
                                               constants.lime_explainer_file_path, date, from_station, to_station,train_num)