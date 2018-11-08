class RomanNumerals:
    def __init__(self):
        pass

    @staticmethod
    def from_roman(roman_value):
        roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        number_list = [0]
        for i in range(0, len(roman_value)):
            to_append = roman_values[roman_value[i]]
            last_value = number_list.pop()
            if last_value >= to_append:
                number_list.append(last_value)
                number_list.append(to_append)
            else:
                number_list.append(to_append - last_value)
        return sum(number_list)

    @staticmethod
    def to_roman(numeral_value):
        number_as_str = []
        for d in str(numeral_value):
            number_as_str.append(d)
        number_as_str = number_as_str[::-1]
        roman_letters = ["I", "V", "X", "L", "C", "D", "M"]
        weight = 0
        for index in range(0, len(number_as_str)):
            actual_val = int(number_as_str[index])
            actual_romans = []
            if weight == 0:
                actual_romans = roman_letters[0:2]
            if weight == 1:
                actual_romans = roman_letters[2:5]
            if weight == 2:
                actual_romans = roman_letters[4:]
            if weight == 3:
                actual_romans = roman_letters[6]
                number_as_str[index] = actual_romans[0] * actual_val
                weight = -1
                continue
            if actual_val == 0:
                number_as_str[index] = ""
            if actual_val < 4:
                number_as_str[index] = actual_romans[0] * actual_val
            if actual_val == 4:
                number_as_str[index] = actual_romans[0] + actual_romans[1]
            if actual_val == 5:
                number_as_str[index] = actual_romans[1]
            if 5 < actual_val < 9:
                number_as_str[index] = actual_romans[1] + actual_romans[0] * (actual_val - 5)
            if actual_val == 9:
                number_as_str[index] = actual_romans[0] + actual_romans[2]
            weight += 1
        number_as_str = number_as_str[::-1]
        return "".join(number_as_str)