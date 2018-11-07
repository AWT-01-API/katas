from src.kevinsanchez.kata_bank.Checksum import Checksum
from src.kevinsanchez.kata_bank.Convert import Convert

"""
class to store in file.
"""
class Store:

    """
    method to create and add the ILL/ERR.
    :param accounts readed from the txt file.
    """
    @staticmethod
    def store_data(accounts):
        new_file = open('../../../stored_accounts.txt', 'w')
        for value in accounts:
            if not Checksum.calculate(value):
                new_file.write(value + "    ILL\n")
            elif not Convert.is_readable(value):
                    new_file.write(value + "    ERR\n")
            else:
                new_file.write(value + "\n")


