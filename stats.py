def count_words(text):
    res = text.split()
    num_words = len(res)

    return num_words


def count_the_number_of_char(text):
    res = {}

    words_split = text.split()

    for i in words_split:
        lowered = i.lower()

        for j in lowered:
            if j not in res:
                res[j] = 1
            else:
                res[j] += 1

    return res
