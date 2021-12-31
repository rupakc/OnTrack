import json
from config import constants


def get_parsed_station_dict_list(json_file_path=constants.station_json_file_path):
    parsed_dict_list = list([])
    with open(json_file_path,'r') as json_file:
        json_string = json_file.read()
    json_dict_list = json.loads(json_string)['features']
    for json_dict in json_dict_list:
        if json_dict['geometry'] is not None and json_dict['properties'] is not None:
            parsed_dict_list.append({'Coordinates': json_dict['geometry']['coordinates'],
                                     'Address': json_dict['properties']['address'],
                                     'Code': json_dict['properties']['code'],
                                     'Name': json_dict['properties']['name'],
                                     'State': json_dict['properties']['state'],
                                     'Zone': json_dict['properties']['zone']})
    return parsed_dict_list


def get_parsed_train_dict_list(json_file_path=constants.train_json_file_path):
    parsed_dict_list = list([])
    with open(json_file_path, 'r') as json_file:
        json_string = json_file.read()
    json_dict_list = json.loads(json_string)['features']
    for json_dict in json_dict_list:
        if json_dict['geometry'] is not None and json_dict['properties'] is not None:
            parsed_dict_list.append({'Coordinates': json_dict['geometry']['coordinates'],
                                     'Third_AC': json_dict['properties']['third_ac'],
                                     'Arrival': json_dict['properties']['arrival'],
                                     'From_Station_Code': json_dict['properties']['from_station_code'],
                                     'Name': json_dict['properties']['name'],
                                     'Zone': json_dict['properties']['zone'],
                                     'Chair_Car': json_dict['properties']['chair_car'],
                                     'First_Class': json_dict['properties']['first_class'],
                                     'Duration_M': json_dict['properties']['duration_m'],
                                     'Sleeper': json_dict['properties']['sleeper'],
                                     'From_Station_Name': json_dict['properties']['from_station_name'],
                                     'Number': json_dict['properties']['number'],
                                     'Departure': json_dict['properties']['departure'],
                                     'Return_Train': json_dict['properties']['return_train'],
                                     'To_Station_Code': json_dict['properties']['to_station_code'],
                                     'Second_AC': json_dict['properties']['second_ac'],
                                     'Classes': json_dict['properties']['classes'],
                                     'To_Station_Name': json_dict['properties']['to_station_name'],
                                     'Duration_H': json_dict['properties']['duration_h'],
                                     'Type': json_dict['properties']['type'],
                                     'First_AC': json_dict['properties']['first_ac'],
                                     'Distance': json_dict['properties']['distance']})
    return parsed_dict_list
