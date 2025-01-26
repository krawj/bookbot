def main():
    file_path = "books/frankenstein.txt"
    file_contents = open_book(file_path)
    word_count = count_words(file_contents)
    character_count = count_chars(file_contents)
    character_count.sort(reverse=True, key=sort_on)
    generate_report(file_path, word_count, character_count)

def open_book(path):
    with open(path) as f:
        return f.read()

def count_words(string):
    words = string.split()
    return len(words)

def count_chars(string):
    chars = {}
    
    for char in string:
        lowercase = char.lower()
        if char.isalpha():
            if lowercase in chars:
                chars[lowercase] += 1
            else:
                chars[lowercase] = 1
    
    char_count_list = [{'name': key, 'num': value} for key, value in chars.items()]

    return char_count_list

def sort_on(dict):
    return dict["num"]

def generate_report(book_file, word_count, character_counts):
    print(f"--- Begin report on {book_file} ---")
    print(f"{word_count} words found in the document")
    print("")

    for dict in character_counts:
        print(f"The character '{dict['name']}' was found {dict['num']} times")

    print("")
    print("--- End report ---")

main()