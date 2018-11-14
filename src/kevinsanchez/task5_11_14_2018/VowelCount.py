
"""
class to count vowels.
"""
class VowelCount:

    """
    get number of vowels.
    :param string to use.
    :return amount of vowels.
    """
    @staticmethod
    def get_count(string):
        counter = 0
        list_vowels = ['a', 'e', 'i', 'o', 'u']
        for vowel in list_vowels:
            counter += string.count(vowel)
        return counter
