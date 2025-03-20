import stats, sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")

    sys.exit(1)

def main(bookname):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")

    stats.get_num_words(bookname)

    print("--------- Character Count -------")

    char_dict = stats.sorted_characters(bookname)

    for char in char_dict:
        if char.isalpha():
            print(f"{char}: {char_dict[char]}")

    print("============= END ===============")

main(sys.argv[1])