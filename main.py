def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def count_words(text):
    res = text.split()
    num_words = len(res)

    return num_words


def main():
    res = get_book_text("./books/frankenstein.txt")
    num_words = count_words(res)

    print(f"{num_words} words found in the document")


main()
