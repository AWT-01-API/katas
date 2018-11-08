import re


class Convertor:
    def __init__(self):
        code0 = [[' ', '_', ' '], ['|', ' ', '|'], ['|', '_', '|']]
        code1 = [[' ', ' ', ' '], [' ', ' ', '|'], [' ', ' ', '|']]
        code2 = [[' ', '_', ' '], [' ', '_', '|'], ['|', '_', ' ']]
        code3 = [[' ', '_', ' '], [' ', '_', '|'], [' ', '_', '|']]
        code4 = [[' ', ' ', ' '], ['|', '_', '|'], [' ', ' ', '|']]
        code5 = [[' ', '_', ' '], ['|', '_', ' '], [' ', '_', '|']]
        code6 = [[' ', '_', ' '], ['|', '_', ' '], ['|', '_', '|']]
        code7 = [[' ', '_', ' '], [' ', ' ', '|'], [' ', ' ', '|']]
        code8 = [[' ', '_', ' '], ['|', '_', '|'], ['|', '_', '|']]
        code9 = [[' ', '_', ' '], ['|', '_', '|'], [' ', '_', '|']]
        self.codeDictionary = {0: code0, 1: code1, 2: code2, 3: code3, 4: code4, 5: code5, 6: code6, 7: code7, 8: code8, 9: code9}

    def getDictKeyByValue(self, valueToFind):
        key = None
        listOfItems = self.codeDictionary.items()
        for item in listOfItems:
            toCompare = item[1]
            if toCompare == valueToFind:
                key = item[0]
                break
        return key

    def reaf_file(self, source):
        with open(source, "r") as f:
            content = f.readlines()

        mat = []
        aux = 0
        for i in range(0, len(content)):
            if aux < 3:
                tmp_value = content[i]
                mat.append(tmp_value)
        aux += 1
        return mat

    def get_raw_code_list(self):
        filedata = self.reaf_file()
        rawCodeList = []
        lastindex = 0
        for lineindex in range(0, int(len(filedata) / 3)):
            nextindex = lastindex + 3
            toAppend = filedata[lastindex:nextindex]
            if len(toAppend) == 3:
                rawCodeList.append(toAppend)
            lastindex = nextindex + 1
        return rawCodeList

    def get_code_matrix_list(self, codelineslist):
        matrix_list = [[], [], [], [], [], [], [], [], [], ]
        lastindex = 0
        for index in range(0, len(matrix_list)):
            nextindex = lastindex + 3
            for line in codelineslist:
                line_to_split = list(line)
                matrix_l = line_to_split[lastindex:nextindex]
                if len(matrix_l) < 3 :
                    matrix_l = [' ', ' ', ' ']
                matrix_list[index].append(matrix_l)
            lastindex = nextindex
        return matrix_list

    def get_all_codes(self):
        codelist = []
        for code in self.get_raw_code_list():
            temp_code = []
            raw_matrix = self.get_code_matrix_list(code)
            for matrix in raw_matrix:
                keyValue = self.getDictKeyByValue(matrix)
                if keyValue is not None:
                    temp_code.append(keyValue)
            codelist.append(temp_code)
        return codelist

    def validate_all_codes(self,codes):
        sum_digit = 0
        op_mult = 1
        for index in range(0, len(codes)):
            raw_matrix = codes[index]
            for code in raw_matrix:
                sum_digit += (op_mult * code)
                op_mult += 1

        is_valid = sum_digit % 11 == 0
        return is_valid
