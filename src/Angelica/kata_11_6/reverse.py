# Reverse every other word in a given string, then return it.
# Don't forget to include the spaces!

def reverse_text(text):
    a = ""
    for i in range(len(text) - 1, 0, -1):
        a += text[i]
    a += text[0]
    return a


def reverse_alternate(string):
    reverse = ""
    words = string.split(" ")

    for x in words:
        reverse += " "
        if len(x) % 2 == 0:
            reverse += reverse_text(x)
        else:
            reverse += x
    return reverse.lstrip()