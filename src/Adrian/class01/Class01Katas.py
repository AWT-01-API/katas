class Class01Factorial:

    def __init__(self):
        pass

    @staticmethod
    def factorial(number):
        fact_int = 1
        for val in range(1, number):
            fact_int *= val
        return fact_int


class Class01Palindrome:

    def __init__(self):
        pass

    @staticmethod
    def palindrome(text):
        for char in range(0, len(text) / 2):
            if text[char] is not text[len(text) - char - 1]:
                return False
        return True


