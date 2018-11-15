class Factorial:
    @staticmethod
    def process(number):
        factorial = number
        while number > 1:
            number = number - 1
            factorial *= number
        return factorial
