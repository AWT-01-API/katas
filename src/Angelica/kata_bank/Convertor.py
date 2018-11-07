import DictionaryNumber
import re

class Convertor:
    def __init__(self):
        self.file = "C:\Users\AngelicaLopez\Desktop\IKata\katas\src\Angelica\kata_bank\source_data.txt"
        self.number = []
        self.cond_position = 0
        self.index_row = 3
        self.index_bytes = 27

    def reaf_file(self):
        with open(".\source_data.txt","r") as f:
            content = f.readlines()

        mat = []
        aux = 0
        for i in range(0,26):
            if aux < 3:
                print (content[i])
                tmp_value = content[i]
                mat.append(tmp_value)
        aux += 1
        return mat

convertor = Convertor()
convertor.reaf_file()




