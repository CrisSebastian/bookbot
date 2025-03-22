from ast import keyword
from stats import word_count
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    book = get_book_text(book_path)
    num_words = word_count(book)
    chars_dict = char_count(book)
    report = gen_report(chars_dict, book_path, num_words)

def char_count(book):
    standarized_book = book.lower()
    characters = {}
    for char in standarized_book:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(dict):
    return dict["num"]

def gen_report(chars_dict, path, amount):
    char_list = []
    print(f"--- Begin report of {path} ---")
    print(f"{amount} words found in the document")
    for char, num in chars_dict.items():
        char_list.append({"char": char, "num": num})

    char_list.sort(reverse=True, key=sort_on)

    for char_dict in char_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["num"]}")
        else:
            pass
    print("--- End of report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
