from kevinsanchez.kata_bank.Convert import Convert
from kevinsanchez.kata_bank.Checksum import Checksum

class Store:

    @staticmethod
    def store_data(accounts):
        new_file = open('../../../stored_accounts.txt', 'w')
        for value in accounts:
            if Checksum.calculate(value):
                new_file.write(value + "\n")
            else:
                new_file.write(value + "    ILL\n")

