from stats import (get_num_words, get_chars_dict, chars_dict_to_sorted_list)
import sys

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(sys.argv) > 1:
        book = sys.argv[1]
    text = get_book_text(book)
    word_count = get_num_words(text)
    char_count = get_chars_dict(text)
    chars_dict = chars_dict_to_sorted_list(char_count)
    print_report(book, word_count, chars_dict)


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def print_report(book_path,num_words,char_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()
