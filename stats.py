def count_words(book_text):
    num_words = 0
    words = book_text.split()
    for word in words:
        num_words += 1
    print(f"{num_words} words found in the document")

def count_character(book_text):
    num_characters = {}
    lowered = book_text.lower()
    for character in lowered:
        if character not in num_characters:
            num_characters[character] = 1
        else:
            num_characters[character] +=1
    print(num_characters)

def sorts_on()