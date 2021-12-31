# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from utils import dbutils, featureutils
from maps import routemap
from explain import generic_explainer
from predict import generic_delay_predictor
from django.http import HttpResponse
import json


def list_stations(request):
    station_list = dbutils.get_list_of_stations()
    response = json.dumps({'station_list': station_list})
    return HttpResponse(response, content_type='application/json')


def get_train_list(request):
    from_station_code = request.GET.get('from')
    to_station_code = request.GET.get('to')
    train_list = dbutils.get_all_train_names_between_stations(from_station_code, to_station_code)
    response = json.dumps({'train_list': train_list})
    return HttpResponse(response, content_type='application/json')


def get_train_route_map(request):
    train_number = request.GET.get('train_num')
    latitude_list, longitude_list = dbutils.get_train_route_coordinates(train_number)
    map_html_string = routemap.get_google_maps_html(latitude_list,longitude_list)
    return HttpResponse(map_html_string)


def get_train_route_map_html_file(request):
    train_number = request.GET.get('train_num')
    latitude_list, longitude_list = dbutils.get_train_route_coordinates(train_number)
    html_server_side_path = routemap.get_google_maps_html_file_path(latitude_list, longitude_list, train_number)
    return HttpResponse(json.dumps({'filepath': html_server_side_path}), content_type='application/json')


def get_train_delay(request):
    date = request.GET.get('date')
    from_station_code = request.GET.get('from')
    to_station_code = request.GET.get('to')
    train_number = request.GET.get('train_num')
    feature_dict = featureutils.get_feature_dictionary(from_station_code, to_station_code, date, train_number)
    delay = generic_delay_predictor.get_delay_in_minutes(feature_dict)
    response = {'delay_minutes': delay%60, 'delay_hours': float(delay/60.0)}
    return HttpResponse(json.dumps(response), content_type='application/json')


def get_delay_explanation(request):
    date = request.GET.get('date')
    from_station_code = request.GET.get('from')
    to_station_code = request.GET.get('to')
    train_number = request.GET.get('train_num')
    feature_dict = featureutils.get_feature_dictionary(from_station_code, to_station_code, date, train_number)
    featureutils.encode_categorical_values(feature_dict)
    feature_list = featureutils.get_feature_list(feature_dict)
    explain_html_string = generic_explainer.get_explanation_for_instance(feature_list)
    return HttpResponse(explain_html_string)


def get_delay_explanation_filepath(request):
    date = request.GET.get('date')
    from_station_code = request.GET.get('from')
    to_station_code = request.GET.get('to')
    train_number = request.GET.get('train_num')
    feature_dict = featureutils.get_feature_dictionary(from_station_code, to_station_code, date, train_number)
    featureutils.encode_categorical_values(feature_dict)
    feature_list = featureutils.get_feature_list(feature_dict)
    explain_html_filepath = generic_explainer.get_explanation_to_file(feature_list, date, from_station_code, to_station_code, train_number)
    return HttpResponse(json.dumps({'filepath': explain_html_filepath}), content_type='application/json')
