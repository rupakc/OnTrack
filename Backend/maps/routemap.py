from gmplot import gmplot
from config import constants
from config import keys


def get_google_maps_html(latitude_tuple, longitude_tuple):
    gmap = gmplot.GoogleMapPlotter(latitude_tuple[len(latitude_tuple)/2], longitude_tuple[len(longitude_tuple)/2], 5, apikey=keys.API_KEYS['google_map_api_key'])
    gmap.plot(latitude_tuple, longitude_tuple, 'cornflowerblue', edge_width=7)
    gmap.draw(constants.map_html_file_path)
    with open(constants.map_html_file_path,'r') as gmap_file:
        map_html_string = gmap_file.read()
    return map_html_string


def get_google_maps_html_file_path(latitude_tuple, longitude_tuple, train_number):
    gmap = gmplot.GoogleMapPlotter(latitude_tuple[len(latitude_tuple) / 2], longitude_tuple[len(longitude_tuple) / 2],
                                   5, apikey=keys.API_KEYS['google_map_api_key'])
    gmap.plot(latitude_tuple, longitude_tuple, 'cornflowerblue', edge_width=7)
    gmap.draw(str(constants.html_output_folder_name + str(train_number) + '.html'))
    return str(constants.google_map_server_side_router_path + str(train_number) + '.html')
