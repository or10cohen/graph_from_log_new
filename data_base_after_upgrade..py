import logging
import time
import linecache
import paramiko
from datetime import datetime
import os
import ast
import colorama
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import shutil
from zipfile import ZipFile
from pathlib import Path
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class make_graps_from_log():
    def __init__(self):
        pass

    def create_directory_if_not_exists(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(Fore.LIGHTBLUE_EX + f'new folder are made: {directory}')

    def create_readme_file(self, SN, ip):
        list_graphs = os.listdir(ip + '/' + SN)
        with open(ip + '/' + SN + '/' + 'read_me.txt', 'w') as f:
            f.write('No. of graphs:  ' + str(len(list_graphs) - 1))
            f.writelines(['\n' + x for x in list_graphs])

    def check_last_update_vs_time_create(self, file_path, IP):
        time_create = datetime.fromtimestamp(os.path.getctime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
        with open(str(IP) + '/' + 'last_update_station: ' + str(IP) + '.txt', 'r') as f:
            last_update = f.read()
        # print(f'time_create > now    -   {time_create} > {last_update}:     {time_create > last_update}')
        # print(f'time_create < now    -   {time_create} < {last_update}:     {time_create < last_update}')
        return time_create < last_update

    def last_update_date(self, IP):
        with open(str(IP) + '/' + 'last_update_station: ' + str(IP) + '.txt', 'w') as f:
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def count_file_with_same_name(self, IP, SN):
        files_list = os.listdir(IP)
        count = [str(SN) in file for file in files_list].count(True)
        return count

    def search_str(self, file_path, find_next_data):

        def order_data(get_data, location_data_inside_lines, count, dict_2_list=False, US=False):
            if US == True:
                get_data = get_data[location_data_inside_lines[count]:-1]
            else:
                get_data = get_data[location_data_inside_lines[count]:]
            get_data = ast.literal_eval(get_data)
            if dict_2_list == True:
                get_data = [get_data]
            len_data = len(get_data)
            for j in range(len_data):
                if US == True:
                    try:
                        get_data[j]['graph_data'][0][0]['curves'][0]['color'] = 'red'
                        data.append(get_data[j])
                    except (TypeError, KeyError) as ErrorA:
                        print(Fore.LIGHTGREEN_EX + str(ErrorA))
                        logging.warning(f"Exception Name: {type(ErrorA).__name__}")
                        logging.warning(f"Exception Desc: {ErrorA}")
                else:
                    data.append(get_data[j])
            return data

        founded_data = {'SN': False, 'end_test': False, 'full_band': False, 'flatness_and_tilt': False,
                        'US': False, 'Error': False}
        location_data_lines, location_data_inside_lines, data = [], [], []
        time.sleep(0.00000001)
        with open(file_path, 'r', encoding='UTF8') as file:
            lines = file.readlines()
            for line in lines:
                if line.find(find_next_data) != -1:
                    location_data_lines.append(lines.index(line))
                    location_data_inside_lines.append(line.find(find_next_data))
        file.close()

        for count, line_a in enumerate(location_data_lines):
            line_a += 1
            get_data = linecache.getline(file_path, line_a).strip()
            if 'serial number is: ' in find_next_data:
                founded_data['SN'] = True
                get_data = get_data[location_data_inside_lines[count]:]
                if 'serial number is:' in get_data:
                    data.append(get_data)
            elif 'Full bandwidth signal' in find_next_data:
                data = order_data(get_data, location_data_inside_lines, count)
                founded_data['full_band'] = True
            elif 'Flatness and Tilt' in find_next_data:
                founded_data['flatness_and_tilt'] = True
                data = order_data(get_data, location_data_inside_lines, count, dict_2_list=True)
            elif 'end of Test UpStream Measurements' in find_next_data:
                founded_data['end_test'] = True
                data.append(get_data)
            elif 'US' in find_next_data:
                founded_data['US'] = True
                data = order_data(get_data, location_data_inside_lines, count, US=True)
            else:
                founded_data['Error'] = True
                print(Fore.LIGHTGREEN_EX + f'Error with search_str() function')
        len_lines = len(lines)
        return data, len_lines, founded_data

    def create_graph(self, data, host, SN):
        # generate each graph present in data
        graph_data_titles = []
        for graph in data:
            graph_data_titles.append(graph["graph_title"])
            print(str(graph["graph_title"] + '  for SN: ' + str(SN)))
            graph_data = graph["graph_data"]
            nbr_vertical_subplot = len(graph_data)
            nbr_horizontal_subplot = max(len(subplot) for subplot in graph_data if subplot is not None)
            fig, axs = plt.subplots(nbr_vertical_subplot, nbr_horizontal_subplot, squeeze=False)
            fig.suptitle(graph["graph_title"])
            for i in range(nbr_vertical_subplot):
                if graph_data[i] is not None:
                    for j in range(nbr_horizontal_subplot):
                        subplot = graph_data[i][j]
                        if subplot is not None:
                            axs[i, j].set_title(subplot["plot_title"])
                            axs[i, j].set_xlabel(subplot["X_axis_label"], color=subplot["X_label_color"])
                            axs[i, j].set_ylabel(subplot["Y_axis_label"], color=subplot["Y_label_color"])
                            for curve in subplot["curves"]:
                                axs[i, j].plot(curve["X_data"], curve["Y_data"], color=curve["color"],
                                               label=curve["curve_name"], linewidth=curve["linewidth"],
                                               marker=curve["marker"], markersize=curve["marker_size"])

                            if any(curve["curve_name"] != "" for curve in subplot["curves"]):
                                axs[i, j].legend()
                            axs[i, j].grid()
            make_graps_from_log.create_directory_if_not_exists(host + '/' + str(SN))
            time.sleep(0.0000001)
            # print(str(SN[:12]))
            plt.savefig(host + '/' + str(SN) + '/' + graph["graph_title"] + ' SN - ' + SN[:12] + ".png")
            # plt.pause(0.1)
            plt.close()
        return graph_data_titles

    def zip_logs(self, host, username, password):
        #------------------------------Paramiko - Open and connect transport-----------------------------------------------#
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        stdin, stdout, stderr = client.exec_command("zip -r debug_logs debug_logs")
        stdout.read().decode()
        print(stdout.read().decode())
        client.close()
        print(Fore.LIGHTGREEN_EX + f'ziping log files in host IP: {host}')
        return stdin, stdout, stderr

    def transfer_zip_file(self, host, username, password, target_folder, local_folder):
        transport = paramiko.Transport((host, 22))
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        # -------------------------------------transfer zip file from remote to host--------------------------------------------
        filepath = target_folder + 'debug_logs.zip'
        localpath = local_folder + '/' + host + '_logs_file.zip'
        sftp.get(filepath, localpath)
        transport.close()
        print(Fore.LIGHTGREEN_EX + f'transferring zip file to local host: {host}')

    def extract_zip_file(self, local_folder):
        print(Fore.LIGHTGREEN_EX + f'starting to extract files from zip in folder: {host}')
        self.path = local_folder + '/' + local_folder + '_logs_file.zip'
        shutil.unpack_archive(self.path, local_folder)


    def delete_zip_file(self, local_folder):
        try:
            os.remove(local_folder + '/' + local_folder + '_logs_file.zip')
        except:
            print(f"{local_folder}/{local_folder}_logs_file.zip already REMOVED")
        print(Fore.LIGHTGREEN_EX + f'deleted zip file in folder: {host}')

    def list_files(self, local_folder):
        folders = os.listdir(local_folder + '/' + 'debug_logs')
        for log_folder in folders:
            path_list = os.listdir(local_folder + '/' + 'debug_logs' + '/' + log_folder)
            for path in path_list:
                data, Log_len, founded_data = make_graps_from_log.search_str(self, local_folder + '/' + 'debug_logs' + '/' + log_folder + '/' + path, 'end of Test UpStream Measurements')
                data2, Log_len2, founded_data2 = make_graps_from_log.search_str(self, local_folder + '/' + 'debug_logs' + '/' + log_folder + '/' + path, 'serial number is: ')
                print('founded_data:        ', founded_data)
                print('founded_data2:        ', founded_data2)
                print('Log_len:        ', Log_len)
                print('Log_len2:        ', Log_len2)


if __name__ == '__main__':
    make_graphs = make_graps_from_log()
    host, username, password = '10.41.42.13', "harmonic", "harmonic"
    target_folder = "/home/harmonic/"
    make_graphs.create_directory_if_not_exists(host)
    local_folder = host
    stdin, stdout, stderr = make_graphs.zip_logs(host, username, password)
    make_graphs.transfer_zip_file(host, username, password, target_folder, host)
    make_graphs.extract_zip_file(local_folder)
    make_graphs.delete_zip_file(local_folder)
    # make_graphs.list_files(local_folder)