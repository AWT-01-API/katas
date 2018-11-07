class Convert:
    """
    traslate matrix into nnnumbers.
    :param matrix from read.
    :return string with the number.
    """
    def traslate(self, matrix):
        j = 0
        list = []
        while j < len(matrix):
            i = 0
            string = ""
            while i < 9:
                if matrix[j][i] is 1 and matrix[j+1][i] is 5 and matrix[j+2][i] is 4:
                    string += "0"
                if matrix[j][i] is 0 and matrix[j+1][i] is 1 and matrix[j+2][i] is 1:
                    string += "1"
                if matrix[j][i] is 1 and matrix[j+1][i] is 2 and matrix[j+2][i] is 3:
                    string += "2"
                if matrix[j][i] is 1 and matrix[j+1][i] is 2 and matrix[j+2][i] is 2:
                    string += "3"
                if matrix[j][i] is 0 and matrix[j+1][i] is 4 and matrix[j+2][i] is 1:
                    string += "4"
                if matrix[j][i] is 1 and matrix[j+1][i] is 3 and matrix[j+2][i] is 2:
                    string += "5"
                if matrix[j][i] is 1 and matrix[j+1][i] is 3 and matrix[j+2][i] is 4:
                    string += "6"
                if matrix[j][i] is 1 and matrix[j+1][i] is 1 and matrix[j+2][i] is 1:
                    string += "7"
                if matrix[j][i] is 1 and matrix[j+1][i] is 4 and matrix[j+2][i] is 4:
                    string += "8"
                if matrix[j][i] is 1 and matrix[j+1][i] is 4 and matrix[j+2][i] is 2:
                    string += "9"
                i += 1
            list.append(string)
            j += 3
        return list

    """
    read and set the matrix.
    :return a list with the number from the file.
    """
    def read(self):
        f = open('../../../source_data.txt', 'r')
        content = f.readlines()
        matrix = []
        i = 1
        j = 0
        while j < len(content):
            if (j is not 0) and ((j+1)%4 is 0):
                j += 1
            row = content[j]
            counter = 9
            row_matrix = []
            while counter > 0:
                if i is 1:
                    if row[:3].__contains__(" _ ") or row[:3].__contains__(" _"):
                        row_matrix.append(1)
                    else:
                        row_matrix.append(0)
                if i is 2:
                    if row[:3].__contains__("  |"):
                        row_matrix.append(1)
                    if row[:3].__contains__(" _|"):
                        row_matrix.append(2)
                    if row[:3].__contains__("|_ "):
                        row_matrix.append(3)
                    if row[:3].__contains__("|_|"):
                        row_matrix.append(4)
                    if row[:3].__contains__("| |"):
                        row_matrix.append(5)
                if i is 3:
                    if row[:3].__contains__("  |"):
                        row_matrix.append(1)
                    if row[:3].__contains__(" _|"):
                        row_matrix.append(2)
                    if row[:3].__contains__("|_ "):
                        row_matrix.append(3)
                    if row[:3].__contains__("|_|"):
                        row_matrix.append(4)
                row = row[3:]
                counter -= 1
            i += 1
            if i is 4:
                i = 1
            matrix.append(row_matrix)
            j += 1
        f.close()
        return self.traslate(matrix)

    """
    main method.
    """
    def readAndTraslate(self):
        print(self.read())