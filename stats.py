def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()

    return file_contents

def get_num_words(path_to_file):
    print(f"Found {len(split_words(path_to_file))} total words")

def split_words(path_to_file):
    text = get_book_text(path_to_file)
    return text.split()

def count_characters(path_to_file):
    from collections import Counter

    string = " ".join(split_words(path_to_file)).lower()

    return Counter(string)

def sorted_characters(path_to_file):
    char_count = count_characters(path_to_file)
    
    return dict(sorted(char_count.items(), key=lambda x: x[1], reverse=True))
