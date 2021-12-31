import parseutils
import commonutils
from config import constants


def insert_station_data_in_db():
    parsed_json_list = parseutils.get_parsed_station_dict_list()
    mongo = commonutils.get_connection(constants.LOCAL_HOST_NAME,constants.PORT_NO,constants.DATABASE_NAME)
    mongo.set_collection(constants.STATION_COLLECTION_NAME)
    for parsed_json in parsed_json_list:
        mongo.insert_document(parsed_json)
    mongo.close_connection()


def insert_train_data_in_db():
    parsed_json_list = parseutils.get_parsed_train_dict_list()
    mongo = commonutils.get_connection(constants.LOCAL_HOST_NAME,constants.PORT_NO,constants.DATABASE_NAME)
    mongo.set_collection(constants.TRAIN_COLLECTION_NAME)
    for parsed_json in parsed_json_list:
        mongo.insert_document(parsed_json)
    mongo.close_connection()


def get_list_of_stations():
    query = dict({})
    parsed_station_list = list([])
    mongo = commonutils.get_connection(constants.LOCAL_HOST_NAME,constants.PORT_NO,constants.DATABASE_NAME)
    mongo.set_collection(constants.STATION_COLLECTION_NAME)
    cursor = mongo.find_document(query)
    for document in cursor:
        parsed_station_list.append({'code': document['Code'], 'name': document['Name']})
    mongo.close_connection()
    return parsed_station_list


def get_all_train_names_between_stations(from_station_code,to_station_code):
    query = dict({'From_Station_Code': from_station_code, 'To_Station_Code': to_station_code})
    parsed_station_list = list([])
    mongo = commonutils.get_connection(constants.LOCAL_HOST_NAME, constants.PORT_NO, constants.DATABASE_NAME)
    mongo.set_collection(constants.TRAIN_COLLECTION_NAME)
    cursor = mongo.find_document(query)
    for document in cursor:
        parsed_station_list.append({'number': document['Number'],'name': document['Name']})
    mongo.close_connection()
    return parsed_station_list


def get_station_coordinates(station_code):
    query_dict = dict({'Code': station_code})
    mongo = commonutils.get_connection(constants.LOCAL_HOST_NAME, constants.PORT_NO, constants.DATABASE_NAME)
    mongo.set_collection(constants.STATION_COLLECTION_NAME)
    cursor = mongo.find_document(query_dict)
    latitude = constants.india_lat
    longitude = constants.india_long
    if cursor is not None:
        for document in cursor:
            longitude = float(document['Coordinates'][0])
            latitude = float(document['Coordinates'][1])
    return latitude, longitude


def get_train_route_coordinates(train_number):
    query = dict({'Number': str(train_number)})
    longitude_list = []
    latitude_list = []
    coordinate_point_list = []
    mongo = commonutils.get_connection(constants.LOCAL_HOST_NAME, constants.PORT_NO, constants.DATABASE_NAME)
    mongo.set_collection(constants.TRAIN_COLLECTION_NAME)
    cursor = mongo.find_document(query)
    for document in cursor:
        coordinate_point_list = document['Coordinates']
    mongo.close_connection()
    for coordinate_point in coordinate_point_list:
        longitude_list.append(coordinate_point[0])
        latitude_list.append(coordinate_point[1])
    return latitude_list, longitude_list
