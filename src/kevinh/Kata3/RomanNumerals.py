class RomanNumerals:
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
        RomanNumerals.number_list_to_roman(number_as_str)
        number_as_str = number_as_str[::-1]
        return "".join(number_as_str)

    @staticmethod
    def number_list_to_roman(number_as_str):
        weight = 0
        for index in range(0, len(number_as_str)):
            actual_val = int(number_as_str[index])
            actual_romans = RomanNumerals.get_actual_romans(weight)
            if weight == 3:
                number_as_str[index] = actual_romans[0] * actual_val
                weight = -1
                continue
            RomanNumerals.transform_number_to_roman(number_as_str, index, actual_val, actual_romans)
            weight += 1

    @staticmethod
    def get_actual_romans(weight):
        roman_letters = ["I", "V", "X", "L", "C", "D", "M"]
        actual_romans = []
        if weight == 0:
            actual_romans = roman_letters[0:2]
        elif weight == 1:
            actual_romans = roman_letters[2:5]
        elif weight == 2:
            actual_romans = roman_letters[4:]
        elif weight == 3:
            actual_romans = roman_letters[6]
        return actual_romans

    @staticmethod
    def transform_number_to_roman(number_as_str, index, actual_val, actual_romans):
        if actual_val == 0:
            number_as_str[index] = ""
        elif actual_val < 4:
            number_as_str[index] = actual_romans[0] * actual_val
        elif actual_val == 4:
            number_as_str[index] = actual_romans[0] + actual_romans[1]
        elif actual_val == 5:
            number_as_str[index] = actual_romans[1]
        elif 5 < actual_val < 9:
            number_as_str[index] = actual_romans[1] + actual_romans[0] * (actual_val - 5)
        elif actual_val == 9:
            number_as_str[index] = actual_romans[0] + actual_romans[2]
