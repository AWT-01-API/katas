class Converter:
    VALUE0 = 0
    VALUE1 = 1
    VALUE2 = 2
    VALUE3 = 3
    VALUE4 = 4
    VALUE5 = 5
    VALUE6 = 6
    VALUE7 = 7
    VALUE8 = 8
    VALUE9 = 9

    CODE0 = [[' ', '_', ' '], ['|', ' ', '|'], ['|', '_', '|']]
    CODE1 = [[' ', ' ', ' '], [' ', ' ', '|'], [' ', ' ', '|']]
    CODE2 = [[' ', '_', ' '], [' ', '_', '|'], ['|', '_', ' ']]
    CODE3 = [[' ', '_', ' '], [' ', '_', '|'], [' ', '_', '|']]
    CODE4 = [[' ', ' ', ' '], ['|', '_', '|'], [' ', ' ', '|']]
    CODE5 = [[' ', '_', ' '], ['|', '_', ' '], [' ', '_', '|']]
    CODE6 = [[' ', '_', ' '], ['|', '_', ' '], ['|', '_', '|']]
    CODE7 = [[' ', '_', ' '], [' ', ' ', '|'], [' ', ' ', '|']]
    CODE8 = [[' ', '_', ' '], ['|', '_', '|'], ['|', '_', '|']]
    CODE9 = [[' ', '_', ' '], ['|', '_', '|'], [' ', '_', '|']]

    def __init__(self, source):
        self.code_dictionary = {self.VALUE0: self.CODE0, self.VALUE1: self.CODE1, self.VALUE2: self.CODE2,
                                self.VALUE3: self.CODE3, self.VALUE4: self.CODE4, self.VALUE5: self.CODE5,
                                self.VALUE6: self.CODE6, self.VALUE7: self.CODE7, self.VALUE8: self.CODE8,
                                self.VALUE9: self.CODE9}
        self.file_path = source

    def get_dict_key_by_value(self, value_find):
        key = None
        for item in self.code_dictionary.items():
            to_compare = item[1]
            if to_compare == value_find:
                key = item[0]
                break
        return key

    def read_file(self):
        with open(self.file_path, "r") as f:
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
                if len(matrix_l) < 3:
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

    def validate_all_codes(self, codes):
        sum_digit = 0
        op_mult = 1
        for index in range(0, len(codes)):
            raw_matrix = codes[index]
            for code in raw_matrix:
                sum_digit += (op_mult * code)
                op_mult += 1
        return sum_digit % 11 == 0
