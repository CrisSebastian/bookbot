from ast import keyword


def main():
    book_path = "books/frankenstein.txt"
    book = get_book_text(book_path)
    num_words = word_count(book)
    chars_dict = char_count(book)
    report = gen_report(chars_dict, book_path, num_words)

def word_count(book):
    words = book.split()
    return len(words)

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
    print(f"{amount} words found in the book")
    for char, num in chars_dict.items():
        char_list.append({"char": char, "num": num})

    char_list.sort(reverse=True, key=sort_on)

    for char_dict in char_list:
        if char_dict["char"].isalpha():
            print(f"The '{char_dict["char"]}' was found {char_dict["num"]} times")
        else:
            pass
    print("--- End of report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
