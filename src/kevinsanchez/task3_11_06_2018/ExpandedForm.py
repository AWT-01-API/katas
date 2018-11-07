"""
expand class.
"""
class ExpandedForm:

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
                final_string += string_value[0] + self.add_zeros(size - 1)
                final_string += " + "
            size -= 1
            string_value = string_value[1:]
        return final_string[:-3]
