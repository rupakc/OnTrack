data_folder_path = '\\Documents\\Github\\OnTrack\\Backend\\data\\'
station_json_filename = 'stations.json'
train_json_filename = 'trains.json'
google_map_location_filename = 'route.html'
model_folder_path = '\\Documents\\Github\\OnTrack\\Backend\\models\\'
delay_model_filename = 'extra_trees_model.pkl'
from_code_encoder_filename = 'from_code_encoder.pkl'
to_code_encoder_filename = 'to_code_encoder.pkl'
lime_explainer_filename = 'lime_explainer.pkl'
html_output_folder_name = '\\Documents\\Github\\OnTrack\\Frontend\\static\\public\\'
google_map_html_filename = 'routemap.html'
lime_explainer_html_filename = 'lime_explain.html'
google_map_server_side_router_path = '/static/public/'
lime_explainer_server_side_router_path = '/static/public/'

station_json_file_path = data_folder_path + station_json_filename
train_json_file_path = data_folder_path + train_json_filename
map_html_file_path = data_folder_path + google_map_location_filename
delay_model_file_path = model_folder_path + delay_model_filename
from_code_encoder_file_path = model_folder_path + from_code_encoder_filename
to_code_encoder_file_path = model_folder_path + to_code_encoder_filename
lime_explainer_file_path = model_folder_path + lime_explainer_filename

EXPIRE_TIME = 1*60*60
DATABASE_NAME = 'Railway'
STATION_COLLECTION_NAME = 'Station'
TRAIN_COLLECTION_NAME = 'Train'
LOCAL_HOST_NAME = 'localhost'
PORT_NO = 27017
NUM_FEATURES = 10

india_lat = 28.6139
india_long = 77.2090


