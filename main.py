def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    print(count_words(file_contents))
    print(count_chars(file_contents))

def count_words(string):
    words = string.split()
    return len(words)

def count_chars(string):
    input = string.lower()
    
    unique_chars = set()
    char_counts = {}

    for char in input:
        unique_chars.add(char)

    for char in unique_chars:
        count = 0
        for letter in input:
            if letter == char:
                count += 1
        char_counts[char] = count
    return char_counts

main()