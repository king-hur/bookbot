def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    print(f"{num_words} words found in the document")
    
    display_num_chars(num_chars)

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_chars(text):
    chars = {}
    words = text.split()
    for word in words: 
        word = word.lower()
        for char in word:
            if char in chars: chars[char] += 1
            else: chars[char] = 1
    return chars        

def display_num_chars(num_chars):
    # alpha_chars = {char: count for char, count in num_chars.items() if char.isalpha()}
    # sorted_chars = sorted(alpha_chars.items(), key=lambda item: item[1], reverse=True)
    for char in num_chars:
        print(f"The '{char}' character was found {num_chars[char]} times")

main()
