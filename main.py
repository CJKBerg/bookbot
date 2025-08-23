def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def main(filepath):
    book_text = get_book_text(filepath)
    return book_text

from stats import count_words
from stats import count_character
count_words(main("books/frankenstein.txt"))
count_character(main("books/frankenstein.txt"))
