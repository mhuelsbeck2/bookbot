from stats import get_word_count
from stats import get_char_count
from stats import get_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def sort_on(items):
    return items["num"]

def main():
    filepath = "books/frankenstein.txt"
    word_count = get_word_count(get_book_text(filepath))
    char_count = get_sorted_list(get_char_count(get_book_text(filepath)))
    char_count.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in char_count:
        ch = dict["char"]
        n = dict["num"]
        if ch.isalpha() == True:
            print(f"{ch}: {n}")
    print("============= END ===============")

main()