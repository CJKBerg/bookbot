import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def main(filepath):
    book_text = get_book_text(filepath)
    return book_text

from stats import count_words
from stats import count_character
from stats import sort_char
from stats import sort_on

# count_words(main("books/frankenstein.txt"))
# count_character(main("books/frankenstein.txt"))
# sort_char(count_character(main("books/frankenstein.txt")))

def print_report(book_path):
    text = main(book_path)
    words = count_words(text)
    print(f"Found {words} total words")
    char_count = count_character(text)
    sorted_chars = sort_char(char_count)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

# print_report("books/frankenstein.txt")

if len(sys.argv) == 2:
    print_report(sys.argv[1])
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)