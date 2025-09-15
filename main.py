from stats import count_words, count_the_number_of_char


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    res = get_book_text("./books/frankenstein.txt")

    word_count = count_words(res)

    char_dict = count_the_number_of_char(res)

    print(word_count)
    print(char_dict)


main()
