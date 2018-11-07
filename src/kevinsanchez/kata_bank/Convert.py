class Convert:
    def read(self):
        f = open('../../../source_data.txt', 'r')
        content = f.readlines()
        i = 1
        matrix = []
        row_matrix = []
        for val in content:
            row = val
            counter = 9
            while counter > 0 and (i is not 4):
                if i is 1:
                    if row[:3].__contains__(" _ "):
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
            #print (row_matrix)
            matrix.insert(0, row_matrix)
            print (matrix[0])
            row_matrix = []
        #print(matrix[0])
        #print(matrix[1])
        #print(matrix[2])
        f.close()