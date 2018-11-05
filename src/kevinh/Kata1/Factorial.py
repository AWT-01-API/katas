class Factorial:
    def __init__(self):
        pass

    def process(self, number):
        factorial = number
        while number > 1:
            number = number - 1
            factorial *= number
        return factorial
