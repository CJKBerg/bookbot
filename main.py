def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def main(filepath):
    book_text = get_book_text(filepath)
    print(book_text)
main("books/frankenstein.txt")
    