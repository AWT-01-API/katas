class Class03:

    @staticmethod
    def expanded_form(num):
        string = ''
        i = 1
        counter = 0
        digits = []
        while num > 0:
            i = i * 10
            if num % i > 1:
                digits.append(num % i)
                num -= num % i
                counter += 1

        while counter > 1:
            string += str(digits[counter - 1]) + " + "
            counter -= 1
        string += str(digits[counter - 1])

        return string


class Class03ReverseAlternate:

    @staticmethod
    def reverse_alternate(string):
        words = string.split(" ")
        rev = ""
        j = False
        for value in words:
            i = len(value) - 1
            aux = ""
            if j:
                while i >= 0:
                    aux += value[i]
                    i -= 1
                rev += aux + ' '
            else:
                rev += value + ' '
            j = not j
        return rev.rstrip()



