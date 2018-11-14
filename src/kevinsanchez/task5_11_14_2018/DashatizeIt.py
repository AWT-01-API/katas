class DashatizeIt:
    @staticmethod
    def dashatize(number):
        if number is None:
            return "None"
        number = abs(number)
        string = ""
        if number is 0:
            return "0"
        while number > 0:
            digit = number % 10
            if digit % 2 is 1:
                string += "-" + str(digit) + "-"
            else:
                string += str(digit)

            number /= 10
        if string[0] is '-':
            string = string[1:]
        if string[len(string) - 1] is '-':
            string = string[:len(string) - 1]
        return string[::-1].replace("--", "-")
