from utils import classificationutils
import lime
import lime.lime_tabular
from config import constants


def train_and_save_explainer(train_set, feature_name_list,class_name_list,categorical_feature_index_list,save_filepath='explainer.bin'):
    explainer = lime.lime_tabular.LimeTabularExplainer(train_set, feature_names=feature_name_list, class_names=class_name_list,
                                                       categorical_features=categorical_feature_index_list, verbose=True,
                                                       mode='regression')
    classificationutils.save_model(save_filepath, explainer)


def get_explanation_html(instance_feature_list,model,num_features,saved_explainer_path):
    explainer = classificationutils.load_model(saved_explainer_path)
    explanation = explainer.explain_instance(instance_feature_list,model.predict,num_features=num_features)
    return explanation.as_html()


def write_explanation_to_file(instance_feature_list,model,num_features,saved_explainer_path, date, from_station, to_station,train_num):
    explainer = classificationutils.load_model(saved_explainer_path)
    explanation = explainer.explain_instance(instance_feature_list, model.predict, num_features=num_features)
    output_filename = str(date) + '_' + str(from_station) + '_' + str(to_station) + '_' + str(train_num) + '.html'
    explanation.save_to_file(constants.html_output_folder_name + output_filename)
    return constants.lime_explainer_server_side_router_path + output_filename

