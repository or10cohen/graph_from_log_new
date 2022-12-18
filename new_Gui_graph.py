import os
import streamlit as st
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
st.set_page_config(layout="wide")
from import_txt import search_str
from graph_data_analyzer import create_graph
import json
import ast
import io
import time

def main():
##----------------------------------------------------------------------------------------------------------------------
##----------------------------------------------main page---------------------------------------------------------------
##-------------------------------------------Grpah GUI for Gen2 log-----------------------------------------------------
##----------------------------------------------------------------------------------------------------------------------
    global Run_Function
    st.title('Graphs from log file')
    if st.button('Run Function'):
        st.write('Running Function')
        Run_Function = 'Run Function'
    else:
        st.write('Press run function to start')
        Run_Function = 'Dont Run Function'

##---------------------------------------------------sidebar------------------------------------------------------------
##-------------------------------------------choose Datatype&Dataset----------------------------------------------------
##----------------------------------------------------------------------------------------------------------------------
    with st.sidebar:
        st.title('choose log.txt')
    #     list_log_from_computer = os.listdir(r'\logs')
    #     log_file_text = st.selectbox(
    #         'choose log.txt',
    #         list_log_from_computer)
    #
    #     uploaded_log_file = st.file_uploader("or upload log text file")
    #     if uploaded_log_file is not None:
    #         st.write("filename:", uploaded_log_file.name)
    #         string_data = io.StringIO(uploaded_log_file.getvalue().decode("utf-8")).read()
    #         text_file = open(r'C:\Users\or_cohen\PycharmProjects\pythonProject\logs\log_' + uploaded_log_file.name, 'w')
    #         text_file.write(string_data)
    #         text_file.close()
    #
    #     st.title('After upload file, please press \'Rerun\' in up-right corner.')


##---------------------------------------------------sidebar------------------------------------------------------------
##-----------------------------------------download files you want to share---------------------------------------------
##----------------------------------------------------------------------------------------------------------------------



##----------------------------------------------------------------------------------------------------------------------
##----------------------------------------------main page---------------------------------------------------------------
##----------------------------------Neural Network - Run Function-------------------------------------------------------
##----------------------------------------------------------------------------------------------------------------------
    if Run_Function == 'Run Function':
        # log_file_path = 'logs\\' + log_file_text
        log_file_path = "105222106473.txt"

#######-----------------------------------------------------------------------------------------------------------#####
        # find_SN = 'phal-util mb SerialNumberGet'
        # find_PN = 'phal-util mb PartNumberGet'
        # find_SN_PN = [find_SN, find_PN]
        # for SN_PN in find_SN_PN:
        #     location_SN_PN_inside_lines, location_SN_PN_lines, SN_PN_datas = search_str(log_file_path, SN_PN)
        #
        # time.sleep(4)
        # st.write('len(location_SN_PN_inside_lines)', len(location_SN_PN_inside_lines))
        # st.write('location_SN_PN_inside_lines', location_SN_PN_inside_lines)
        # st.write('len(location_SN_PN_lines)', len(location_SN_PN_lines))
        # st.write('location_SN_PN_lines', location_SN_PN_lines)
        # st.write('len(SN_PN_datas)', len(SN_PN_datas))
        # st.write('SN_PN_datas', SN_PN_datas)
#######-----------------------------------------------------------------------------------------------------------#####

        # find_next_data1 = "{'graph_title': 'Curve"  # INCLUD 2
        find_next_data3 = "{'graph_title': 'DS1 Flatness and Tilt 0"
        find_next_data4 = "{'graph_title': 'DS1 Flatness and Tilt 7.0"
        find_next_data5 = "{'graph_title': 'DS1 Flatness and Tilt 13.0"
        find_next_data6 = "{'graph_title': 'DS2 Flatness and Tilt 0"
        find_next_data7 = "{'graph_title': 'DS2 Flatness and Tilt 7.0"
        find_next_data8 = "{'graph_title': 'DS2 Flatness and Tilt 13.0"
        find_next_data9 = "{'graph_title': 'US1"  # INCLUD US2, US3, US4
        find_next_data2 = "[{'graph_title': 'DS1 Full bandwidth signal"  # INCLUD DS2
        find_next_datas = [find_next_data2, find_next_data3, find_next_data4, find_next_data5,
                           find_next_data6, find_next_data7, find_next_data8, find_next_data9]
        for find_next_data in find_next_datas:
            location_data_inside_lines, location_data_lines, datas = search_str(log_file_path, find_next_data)
            for data in datas:
                create_graph([data])
        time.sleep(3)


##------------------------------------------main page------------------------------------------------------------------
##----------------------------------------tabs and Graphs---------------------------------------------------------------
##----------------------------------------------------------------------------------------------------------------------
        tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(
        ["DS1 bandwidth", "DS2 bandwidth"
        , 'DS1 Flatness & Tilt 0', 'DS1 Flatness & Tilt 7', 'DS1 Flatness & Tilt 13'
        , 'DS2 Flatness & Tilt 0', 'DS2 Flatness & Tilt 7', 'DS2 Flatness & Tilt 13'])

        with tab1:
            st.header("DS1 signal")
            # NN_graph = Image.open('DS1 Flatness and Tilt 0.0.png')
            st.image('DS1 Full bandwidth signal.png', caption='DS1 Full bandwidth signal.png')
        with tab2:
            st.header("DS2 signal")
            # LossFunctionPerEpoch = Image.open('DS1 Flatness and Tilt 0.0.png')
            st.image('DS2 Full bandwidth signal.png', caption='DS2 Full bandwidth signal.png')
        with tab3:
            st.header("DS1 Flatness & Tilt 0")
            # NN_graph = Image.open('DS1 Flatness and Tilt 0.0.png')
            st.image('DS1 Flatness and Tilt 0.0.png', caption='DS1 Flatness and Tilt 0.0.png')
        with tab4:
            st.header("DS1 Flatness & Tilt 7")
            # NN_graph = Image.open('DS1 Flatness and Tilt 0.0.png')
            st.image('DS1 Flatness and Tilt 7.0.png', caption='DS1 Flatness and Tilt 7.0.png')
        with tab5:
            st.header("DS1 Flatness & Tilt 13")
            # NN_graph = Image.open('DS1 Flatness and Tilt 0.0.png')
            st.image('DS1 Flatness and Tilt 13.0.png', caption='DS1 Flatness and Tilt 13.0.png')
        with tab6:
            st.header("DS2 Flatness & Tilt 0")
            # NN_graph = Image.open('DS1 Flatness and Tilt 0.0.png')
            st.image('DS2 Flatness and Tilt 0.0.png', caption='DS2 Flatness and Tilt 0.0.png')
        with tab7:
            st.header("DS2 Flatness & Tilt 7")
            # NN_graph = Image.open('DS1 Flatness and Tilt 0.0.png')
            st.image('DS2 Flatness and Tilt 7.0.png', caption='DS2 Flatness and Tilt 7.0.png')
        with tab8:
            st.header("DS2 Flatness & Tilt 13")
            # NN_graph = Image.open('DS1 Flatness and Tilt 0.0.png')
            st.image('DS2 Flatness and Tilt 13.0.png', caption='DS2 Flatness and Tilt 13.0.png')

        tab1, tab2, tab3, tab4, tab5= st.tabs(["US1", "US2", "US3", "US4", "Python code"])
        with tab1:
            st.header("US1")
            # NN_graph = Image.open('DS1 Flatness and Tilt 0.0.png')
            st.image('US1 calibration measurement.png', caption='US1 calibration measurement.png')
            st.image('US1 nominal measurement.png', caption='US1 nominal measurement.png')
            st.image('US1 spurious measurement.png', caption='US1 spurious measurement.png')
        with tab2:
            st.header("US2")
            # NN_graph = Image.open('DS1 Flatness and Tilt 0.0.png')
            st.image('US2 calibration measurement.png', caption='US2 calibration measurement.png')
            st.image('US2 nominal measurement.png', caption='US2 nominal measurement.png')
            st.image('US2 spurious measurement.png', caption='US2 spurious measurement.png')
        with tab3:
            st.header("US3")
            # NN_graph = Image.open('DS1 Flatness and Tilt 0.0.png')
            st.image('US3 calibration measurement.png', caption='US3 calibration measurement.png')
            st.image('US3 nominal measurement.png', caption='US3 nominal measurement.png')
            st.image('US3 spurious measurement.png', caption='US3 spurious measurement.png')
        with tab4:
            st.header("US4")
            # NN_graph = Image.open('DS1 Flatness and Tilt 0.0.png')
            st.image('US4 calibration measurement.png', caption='US4 calibration measurement.png')
            st.image('US4 nominal measurement.png', caption='US4 nominal measurement.png')
            st.image('US4 spurious measurement.png', caption='US4 spurious measurement.png')
        with tab5:
            st.header("Python Code")
            # st.code(open("graph_data_analyzer.py").read(), language="python")

    elif Run_Function == 'Dont Run Function':
        print('press run function')
    else:
        print('Error with running button')

##-----------------------------------------------------------------------------------------------------------
main()



