from stats import get_word_count
from stats import get_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    filepath = "books/frankenstein.txt"
    word_count = get_word_count(get_book_text(filepath))
    char_count = get_char_count(get_book_text(filepath))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print(char_count)
    print("============= END ===============")

main()