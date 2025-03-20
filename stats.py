def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def get_num_words():
    print(f"Found {len(split_words())} total words")

def split_words():
    text = get_book_text("books/frankenstein.txt")
    return text.split()

def count_characters():
    from collections import Counter

    string = " ".join(split_words()).lower()

    return Counter(string)

def sorted_characters():
    char_count = count_characters()
    
    return dict(sorted(char_count.items(), key=lambda x: x[1], reverse=True))
