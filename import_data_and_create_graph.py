import numpy as np
from graph_data_analyzer import create_graph
from import_txt import search_str
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import json
import ast
import os

list = []


log_file_path = "105222106473.txt"
find_next_data1 = "{'graph_title': 'Curve"  # INCLUD 2
find_next_data3 = "{'graph_title': 'DS1 Flatness and Tilt 0"
find_next_data4 = "{'graph_title': 'DS1 Flatness and Tilt 7.0"
find_next_data5 = "{'graph_title': 'DS1 Flatness and Tilt 13.0"
find_next_data6 = "{'graph_title': 'DS2 Flatness and Tilt 0"
find_next_data7 = "{'graph_title': 'DS2 Flatness and Tilt 7.0"
find_next_data8 = "{'graph_title': 'DS2 Flatness and Tilt 13.0"
find_next_data9 = "{'graph_title': 'US1"  # INCLUD US2, US3, US4
find_next_data2 = "[{'graph_title': 'DS1 Full bandwidth signal" # INCLUD DS2
find_next_datas = [find_next_data2, find_next_data3, find_next_data4, find_next_data5, find_next_data6
                   , find_next_data7, find_next_data8, find_next_data9]
for find_next_data in find_next_datas:
    location_data_inside_lines, location_data_lines, datas = search_str(log_file_path, find_next_data)
    print(Fore.GREEN + str(location_data_lines))
    print(Fore.GREEN + str(location_data_inside_lines))
    print(Fore.GREEN + str(len(location_data_lines)))
    print(Fore.GREEN + str(type(datas)))
    # print(Fore.GREEN + str(type(datas[0])))
    # print(data[0])
    for data in datas:
        # list.append(data['graph_data'][0][0]['curves'][0]['Y_data'])
        # print(data['graph_data'][0][0]['curves'][0]['Y_data'])
        create_graph([data])

# for i in range(len(list) - 1, -1, -1):
#     print(abs(np.array(list[i]) - np.array(list[i -1])))











