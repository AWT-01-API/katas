"""
class for checksum.
"""
class Checksum:

    """
    method which calculate the checksum.
    :param number to check.
    :return true is success.
    """
    @staticmethod
    def calculate(number):
        counter = 1
        check_sum = 0
        for value in number:
            check_sum += int(value)*counter
            if check_sum % 11 == 0:
                return True
            else:
                return False
