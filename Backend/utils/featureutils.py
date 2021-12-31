from . import dbutils,classificationutils
import numpy as np
from config import constants


def get_feature_dictionary(from_station_code,to_station_code,date_string,train_number):
    from_latitude, from_longitude = dbutils.get_station_coordinates(from_station_code)
    to_latitude, to_longitude = dbutils.get_station_coordinates(to_station_code)
    train_number = int(train_number)
    date_list = date_string.split('-')
    year = int(date_list[0])
    month = int(date_list[1])
    day = int(date_list[2])

    feature_dict = dict({'from_code': from_station_code,
                         'to_code': to_station_code,
                         'day': day,
                         'month': month,
                         'year': year,
                         'from_lat': from_latitude,
                         'from_lng': from_longitude,
                         'to_lat': to_latitude,
                         'to_lng': to_longitude,
                         'number': train_number})
    return feature_dict


def get_feature_list(feature_dict):
    feature_list = list([])
    feature_list.append(feature_dict['from_code'])
    feature_list.append(feature_dict['from_lat'])
    feature_list.append(feature_dict['from_lng'])
    feature_list.append(feature_dict['number'])
    feature_list.append(feature_dict['to_code'])
    feature_list.append(feature_dict['to_lat'])
    feature_list.append(feature_dict['to_lng'])
    feature_list.append(feature_dict['day'])
    feature_list.append(feature_dict['month'])
    feature_list.append(feature_dict['year'])
    return np.array(feature_list)


def encode_categorical_values(feature_dictionary):
    from_code_encoder = classificationutils.load_model(constants.from_code_encoder_file_path)
    to_code_encoder = classificationutils.load_model(constants.to_code_encoder_file_path)
    if feature_dictionary['from_code'] in from_code_encoder.classes_:
        feature_dictionary['from_code'] = from_code_encoder.transform([feature_dictionary['from_code']])[0]
    else:
        feature_dictionary['from_code'] = len(from_code_encoder.classes_)

    if feature_dictionary['to_code'] in to_code_encoder.classes_:
        feature_dictionary['to_code'] = to_code_encoder.transform([feature_dictionary['to_code']])[0]
    else:
        feature_dictionary['to_code'] = len(to_code_encoder.classes_)
