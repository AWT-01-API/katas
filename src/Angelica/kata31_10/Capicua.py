def is_capicua(value):
    word = str(value)

    index = -1
    same = 0

    for x in range(0,len(word)/2):

        if word[x] == word[index]:
            same = same+1
        index = index - 1

    return same == (len(word) / 2)
