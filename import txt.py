import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def search_str(file_path, first_word):
    NumberDataLines = []
    Datalines = []
    with open(file_path, 'r') as file:
        # read all content of a file
        content = file.read()
        # check if string present in a file
        if first_word in content:
            print(Fore.GREEN + 'first_word exist in a file')
        else:
            print(Fore.RED + 'first_word does not exist in a file')
    file.close()

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # check if string present on a current line
            if line.find(first_word) != -1:
                # print(first_word, 'string exists in file')
                # print('Line Number:', lines.index(line))
                #print('Line:', line)
                NumberDataLines.append(lines.index(line))
                Datalines.append(line)
    file.close()
    return NumberDataLines, Datalines

if __name__ == '__main__':
    logFileText = "log.txt"
    firstTextSearch = "graph_title"
    NumberDataLines, DataLines = search_str(logFileText, firstTextSearch)
    print(Fore.GREEN + str(NumberDataLines))
    print(Fore.GREEN + str(len(DataLines)))