"""
reverse class.
"""
class ReverseWord:

    """
    method which reverse odd positions.
    :param phrase to reverse.
    :return phrase with resersed words.
    """
    def reverse_alternate(self, phrase):
        words = phrase.split(" ")
        new_phrase = ""
        size = len(words)
        i = 0
        while size > i:
            if i%2 is not 0:
                words[i] = words[i][::-1]
            new_phrase += words[i] + " "
            i += 1
        return new_phrase[:-1]
