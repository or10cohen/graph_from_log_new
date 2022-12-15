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
##----------------------------------Neural Network - by Oren Niazov-----------------------------------------------------
##----------------------------------------------------------------------------------------------------------------------
    global Run_Function, Dataset
    st.title('Graph from log file')

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
        list_log_from_computer = os.listdir(r'C:\Users\or_cohen\PycharmProjects\pythonProject\logs')
        logFileText = st.selectbox(
            'choose log.txt',
            list_log_from_computer)

        # uploaded_log_file = st.file_uploader("or upload log text file")
        # if uploaded_log_file is not None:
        #     st.write("filename:", uploaded_log_file.name)
        #     string_data = io.StringIO(uploaded_log_file.getvalue().decode("utf-8")).read()
        #     text_file = open(r'C:\Users\or_cohen\PycharmProjects\pythonProject\logs\log_' + uploaded_log_file.name, 'w')
        #     text_file.write(string_data)
        #     text_file.close()

##---------------------------------------------------sidebar------------------------------------------------------------
##-----------------------------------------download files you want to share---------------------------------------------
##----------------------------------------------------------------------------------------------------------------------
        # with open("graph_data_analyzer.py") as file:
        #     btn = st.download_button(
        #         label="Download graph_data_analyzer.py Python Resources File",
        #         data=file,
        #     )
        #
        # with open("import_txt.py") as file:
        #     btn = st.download_button(
        #         label="Download import_txt Python Resources File",
        #         data=file,
        #     )

##----------------------------------------------------------------------------------------------------------------------
##----------------------------------------------main page---------------------------------------------------------------
##----------------------------------Neural Network - Run Function-------------------------------------------------------
##----------------------------------------------------------------------------------------------------------------------
    if Run_Function == 'Run Function':
        log_file_path = "log.txt"
        find_next_data = "{'graph_title': 'DS1 Flatness and Tilt"
        location_data_inside_lines, location_data_lines, dates = search_str(log_file_path, find_next_data)
        for data in dates:
            create_graph([data])

##-------------------------------------------main page------------------------------------------------------------------
##----------------------------------------tabs and Graphs---------------------------------------------------------------
##----------------------------------------------------------------------------------------------------------------------

        time.sleep(10)
        # # st.image('graphs\DS1 Flatness and Tilt 0.0.png', caption='graphs\DS1 Flatness and Tilt 0.0.png')
        tab1, tab2, tab3, tab4 = st.tabs(["DS1 Flatness and Tilt 0.0", "DS1 Flatness and Tilt 7.0"
                                       ,"DS1 Flatness and Tilt 13.0", "Python code"])
        with tab1:
            st.header("DS1 Flatness and Tilt 0.0.png")
            # NN_graph = Image.open('graphs\DS1 Flatness and Tilt 0.0.png')
            st.image('graphs\DS1 Flatness and Tilt 0.0.png', caption='graphs\DS1 Flatness and Tilt 0.0.png')

        with tab2:
            st.header("DS1 Flatness and Tilt 7.0.png")
            # LossFunctionPerEpoch = Image.open('graphs\DS1 Flatness and Tilt 0.0.png')
            st.image('graphs\DS1 Flatness and Tilt 0.0.png', caption='graphs\DS1 Flatness and Tilt 7.0.png')
        with tab3:
            st.header("DS1 Flatness and Tilt 13.0.png")
            # NN_graph = Image.open('graphs\DS1 Flatness and Tilt 0.0.png')
            st.image('graphs\DS1 Flatness and Tilt 0.0.png', caption='graphs\DS1 Flatness and Tilt 13.0.png')

        with tab4:
            st.header("Python Code")
        st.code(open("graph_data_analyzer.py").read(), language="python")

    elif Run_Function == 'Dont Run Function':
        print('press run function')
    else:
        print('Error with running button')


##-----------------------------------------------------------------------------------------------------------
main()



