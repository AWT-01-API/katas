"""
class calculate.
"""
class Calculate:

    """
    calculates the factorial of a positive number.
    :param number
    :return factorial.
    """
    def fact(self, number):
        if number == 1:
            return 1
        else:
            return number * self.fact(number - 1)

    """
    verifies if is capicua.
    :param word
    :return true if is capicua.
    """
    def is_capicua(self, word):
        return word[::-1] == word


