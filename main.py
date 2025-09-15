def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    res = get_book_text("./books/frankenstein.txt")

    print(res)


main()
