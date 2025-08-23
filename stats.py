def count_words(book_text):
    num_words = 0
    words = book_text.split()
    for word in words:
        num_words += 1
    return num_words

def count_character(book_text):
    num_characters = {}
    lowered = book_text.lower()
    for character in lowered:
        if character not in num_characters:
            num_characters[character] = 1
        else:
            num_characters[character] +=1
    return num_characters

def sort_on(item):
    return item["num"]

def sort_char(characters):
    sorted_characters = []
    for char, count in characters.items():
        if char.isalpha():
            sorted_characters.append({
                "char": char,
                "num": count
            })
    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters