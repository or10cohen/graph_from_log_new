import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import linecache
import ast

def search_str(file_path, find_next_data):
    location_data_lines = []
    location_data_inside_lines = []
    data = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # check if string present on a current line
            if line.find(find_next_data) != -1:
                location_data_lines.append(lines.index(line))
                location_data_inside_lines.append(line.find(find_next_data))
        # print(location_data_lines)
        # print(location_data_inside_lines)
    file.close()

    for count, line_a in enumerate(location_data_lines):
        line_a += 1
        get_data = linecache.getline(file_path, line_a).strip()
        if 'Full bandwidth signal' in find_next_data:
            get_data = get_data[location_data_inside_lines[count]:]
            get_data = ast.literal_eval(get_data)
            len_data = len(get_data)
            for i in range(len_data):
                data.append(get_data[i])
        elif 'Flatness and Tilt' in find_next_data:
            get_data = get_data[location_data_inside_lines[count]:]
            get_data = ast.literal_eval(get_data)
            get_data = [get_data]
            len_data = len(get_data)
            for i in range(len_data):
                data.append(get_data[i])
#########---------------------------------------------------------------------------------------------------------######
        # elif 'phal-util'in find_next_data:
        #     get_data = get_data[location_data_inside_lines[count]:]
        #     print('get_data', get_data)
        #     print('type(get_data)', type(get_data))
        #     len_data = len(get_data)
        #     print('len(get_data)', len(get_data))
        #     for i in range(len_data):
        #         data.append([get_data[i]])
        #         print('len(data)', len(data))
#########---------------------------------------------------------------------------------------------------------######
        else:
            get_data = get_data[location_data_inside_lines[count]:-1]
            get_data = ast.literal_eval(get_data)
            len_data = len(get_data)
            for i in range(len_data):
                # print(get_data[i])
                # print(type(get_data[i]))
                get_data[i]['graph_data'][0][0]['curves'][0]['color'] = 'red'
                data.append(get_data[i])
    return location_data_inside_lines, location_data_lines, data

if __name__ == '__main__':
    log_file_path = '105222223221.txt'
    # find_next_data = "{'graph_title': 'DS1 Flatness and Tilt 0"
    # location_data_inside_lines, location_data_lines, data = search_str(log_file_path, find_next_data)
    # print(Fore.GREEN + str(location_data_lines))
    # print(Fore.GREEN + str(location_data_inside_lines))
    # print(Fore.GREEN + str(len(location_data_lines)))
    # print(type(data))
    # # print(type(data[0]))
    # # print(data[0])

########_-----------------------------------------------------------------------------------------------#####

    find_SN = 'phal-util mb SerialNumberGet'
    find_PN = 'phal-util mb PartNumberGet'
    find_SN_PN = [find_SN, find_PN]
    for SN_PN in find_SN_PN:
        location_SN_PN_inside_lines, location_SN_PN_lines, SN_PN_datas = search_str(log_file_path, SN_PN)
    print('location_SN_PN_inside_lines', location_SN_PN_inside_lines)
    print('location_SN_PN_lines', location_SN_PN_lines)
    print('SN_PN_datas', SN_PN_datas)


