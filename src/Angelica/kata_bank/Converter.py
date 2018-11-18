class Codes:
    VALUES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    MATRIX = [[[' ', '_', ' '], ['|', ' ', '|'], ['|', '_', '|']],
              [[' ', ' ', ' '], [' ', ' ', '|'], [' ', ' ', '|']],
              [[' ', '_', ' '], [' ', '_', '|'], ['|', '_', ' ']],
              [[' ', '_', ' '], [' ', '_', '|'], [' ', '_', '|']],
              [[' ', ' ', ' '], ['|', '_', '|'], [' ', ' ', '|']],
              [[' ', '_', ' '], ['|', '_', ' '], [' ', '_', '|']],
              [[' ', '_', ' '], ['|', '_', ' '], ['|', '_', '|']],
              [[' ', '_', ' '], [' ', ' ', '|'], [' ', ' ', '|']],
              [[' ', '_', ' '], ['|', '_', '|'], ['|', '_', '|']],
              [[' ', '_', ' '], ['|', '_', '|'], [' ', '_', '|']]]


class Converter:
    def __init__(self, source):
        self.file_path = source

    def get_dict_key_by_value(self, value_find):
        key = None
        for index in range(0, len(Codes.MATRIX)):
            to_compare = Codes.MATRIX[index]
            if to_compare == value_find:
                key = Codes.VALUES[index]
                break
        return key

    def read_file(self):
        with open(self.file_path, "rb") as f:
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
                matrix_l = [s.replace('\r', ' ') for s in matrix_l]
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
                else:
                    temp_code.append("?")
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

    def save_converted_codes(self, name):
        code_file = open(name + ".txt", "w+")
        code_list = self.get_all_codes()
        for line in range(0, len(code_list)):
            if "?" in code_list[line]:
                code_file.write(''.join(str(e) for e in code_list[line]) + " ILL\n")
            else:
                code_file.write(''.join(str(e) for e in code_list[line]) + "\n")
        code_file.close()
