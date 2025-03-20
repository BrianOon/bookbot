import stats

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    stats.get_num_words()
    print("--------- Character Count -------")

    char_dict = stats.sorted_characters()

    for char in char_dict:
        if char.isalpha():
            print(f"{char}: {char_dict[char]}")

    print("============= END ===============")

main()