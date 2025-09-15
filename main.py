from stats import count_words, count_the_number_of_char, get_sorted_list


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    res = get_book_text("./books/frankenstein.txt")

    word_count = count_words(res)

    char_dict = count_the_number_of_char(res)

    res = get_sorted_list(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count ----------")
    for i in res:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")


main()
