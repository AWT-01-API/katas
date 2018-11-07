
from src.kevinsanchez.kata_bank.File_route import File_route
"""
convert from |_ to numbers.
"""
class Convert:

    """
    traslate matrix into numbers.
    :param matrix from read.
    :return string with the number.
    """
    def traslate(self, matrix):
        row = 0
        final_list = []
        map_numbers = {"165": "0",
                       "022": "1",
                       "134": "2",
                       "133": "3",
                       "052": "4",
                       "143": "5",
                       "145": "6",
                       "122": "7",
                       "155": "8",
                       "153": "9"}
        while row < len(matrix):
            column = 0
            string = ""
            while column < 9:
                key = matrix[row][column] + matrix[row+1][column] + matrix[row+2][column]
                if key in map_numbers:
                    string += map_numbers.get(key)
                else:
                    string += "?"
                column += 1
            final_list.append(string)
            row += 3
        return final_list

    """
    compare the patter found.
    :return the value given to the pattern.
    """
    def compare(self, string):
        map_pattern = {"   ": "0",
                       " _ ": "1",
                       "  |": "2",
                       " _|": "3",
                       "|_ ": "4",
                       "|_|": "5",
                       "| |": "6"}

        if string in map_pattern:
            return map_pattern.get(string)

    """
    read the file.
    :return a list with rows of the file.
    """
    def read(self):
        find_route = File_route()
        file_to_read = open(find_route.find(), 'r')
        content = file_to_read.readlines()
        file_to_read.close()
        return content

    """
    this method extract rows except blank spaces.
    :return a list with final number.
    """
    def extract(self):
        matrix = []
        row_counter = 0
        content = self.read()
        while row_counter < len(content):
            if (row_counter is not 0) and ((row_counter + 1) % 4 is 0):
                row_counter += 1
            row = content[row_counter]
            counter = 9
            row_matrix = []
            while counter > 0:
                row_matrix.append(self.compare(row[:3]))
                row = row[3:]
                counter -= 1
            matrix.append(row_matrix)
            row_counter += 1
        return self.traslate(matrix)

