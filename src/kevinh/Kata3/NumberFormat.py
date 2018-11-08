class NumberFormat:
    def __init__(self):
        pass

    @staticmethod
    def expanded_form(number):
        result = []
        value = []
        for digit in str(number):
            value.append (int(digit))
        value = value[::-1]
        for index in range(0, len(value)):
            number = value[index]
            result.append(str(number*10**index))
        result = result[::-1]
        while "0" in result:
            result.remove("0")
        return " + ".join(result)