import re


class Convertor:
    def __init__(self, source):
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
        self.code_dictionary = {0: code0, 1: code1, 2: code2, 3: code3, 4: code4, 5: code5, 6: code6, 7: code7, 8: code8, 9: code9}
        self.source = source

    def get_dict_key_by_value(self, value_find):
        key = None
        list_items = self.code_dictionary.items()
        for item in list_items:
            to_compare = item[1]
            if to_compare == value_find:
                key = item[0]
                break
        return key

    def read_file(self):
        with open(self.source, "r") as f:
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
        filedata = self.read_file()
        raw_code_list = []
        lastindex = 0
        for lineindex in range(0, int(len(filedata) / 3)):
            nextindex = lastindex + 3
            to_append = filedata[lastindex:nextindex]
            if len(to_append) == 3:
                raw_code_list.append(to_append)
            lastindex = nextindex + 1
        return raw_code_list

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
                key_value = self.get_dict_key_by_value(matrix)
                if key_value is not None:
                    temp_code.append(key_value)
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
