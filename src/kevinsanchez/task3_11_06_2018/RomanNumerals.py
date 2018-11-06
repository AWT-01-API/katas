"""
class for convesion.
"""
class RomanNumerals:

    """
    constructor.
    """
    def __init__(self):
        self.mapp = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

    """
    add zeros depend of the position.
    """
    def add_zeros(self, amount):
        string = ""
        while amount > 0:
            string += "0"
            amount -= 1
        return string

    """
    convert a number from 123 to 100 20 3.
    :param value number to convert.
    :return a string with the numbers.
    """
    def expand(self, value):
        string_value = str(value)
        size = len(string_value)
        final_string = ""
        while size > 0:
            if string_value[0] is not "0":
                final_string += string_value[0] + self.add_zeros(size-1)
                final_string += " "
            size -= 1
            string_value = string_value[1:]
        return final_string[:-1]

    """
    conversion without special cases.
    :param number to convert.
    :return string.
    """
    def raw_conversion(self, number):
        string = self.expand(number).split(" ")
        list = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
        final_string = ""
        for val in string:
            i = 0
            new_val = int(val)
            new_string = ""
            while new_val > 0:
                if new_val >= self.mapp.get(list[i]):
                    new_string += list[i]
                    new_val -= self.mapp.get(list[i])
                else:
                    i += 1
            final_string += new_string
        return final_string

    """
    method to convert a number to roman.
    :param number to convert.
    :return the roman number.
    """
    def to_roman(self, number):
        string = self.raw_conversion(number)
        if string.__contains__("DCCCC"):
            string = string.replace("DCCCC", "CM")
        if string.__contains__("CCCC"):
            string = string.replace("CCCC", "CD")
        if string.__contains__("LXXXX"):
            string = string.replace("LXXXX", "XC")
        if string.__contains__("XXXX"):
            string = string.replace("XXXX", "XL")
        if string.__contains__("VIIII"):
            string = string.replace("VIIII", "IX")
        if string.__contains__("IIII"):
            string = string.replace("IIII", "IV")
        return string

    """
    helps to convert cases like IX, IV, etc.
    :param f_number first number in special cases.
    :param s_number second number in special cases.
    :return the final number of the cases. 
    """
    def helper(self, f_number, s_number):
        if f_number < s_number:
            return s_number-f_number
        else:
            return f_number+s_number

    """
    convert from roman to decimal.
    :param string roman number.
    :return decimal number.
    """
    def from_roman(self, string):
        size = len(string)
        number = 0
        while size > 1:
            f = self.mapp.get(string[size-2])
            s = self.mapp.get(string[size-1])
            number += self.helper(f, s)
            size -= 2
        if size is 1:
            return number+self.mapp.get(string[0])
        else:
            return number
