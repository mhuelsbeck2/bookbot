def get_word_count(book_text):
    words = book_text.split()
    return len(words)

def get_char_count(book_text):
    char_count = {}
    book_text = book_text.lower()
    for ch in book_text:
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1
    return char_count
        