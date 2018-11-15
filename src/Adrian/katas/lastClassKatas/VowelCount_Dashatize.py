class VowelCount:

    @staticmethod
    def get_count(inputStr):
        vowels = b'aeiou'
        return len(inputStr) - len(inputStr.translate(None, vowels))


class Dashatize:
    @staticmethod
    def dashatize(num):
        dnum = ""
        if num is None:
            return 'None'
        for i in str(abs(num)):
            if int(i) % 2:
                dnum = dnum + ('-' + i + '-')
            else:
                dnum = dnum + i
        return dnum.replace('--', '-').strip('-')

    """ First solution
    snum = str(num)
    for n, odd in {"1": "-1-", "3": "-3-", "5": "-5-", "7": "-7-", "9": "-9-"}.items():
        snum = snum.replace(n, odd)
    snum = snum.replace('--', '-').strip('-')
    return snum
    """

