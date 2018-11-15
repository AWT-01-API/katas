class NumberFormat:
    @staticmethod
    def expanded_form(number):
        result = []
        value = NumberFormat.number_to_list(number)
        value = value[::-1]
        for index in range(0, len(value)):
            number = value[index]
            result.append(str(number*10**index))
        result = result[::-1]
        return " + ".join(NumberFormat.remove_all("0", result))

    @staticmethod
    def remove_all(item, list_to_remove):
        while item in list_to_remove:
            list_to_remove.remove(item)
        return list_to_remove

    @staticmethod
    def number_to_list(number):
        value = []
        for digit in str(number):
            value.append(int(digit))
        return value
