def count_letters(string):
    word = string.lower()
    letter_counts = {}
    for letter in word:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    return letter_counts


def main():
    string = input("Enter Word: ")
    letter_counts = count_letters(string)
    print(letter_counts)


if __name__ == "__main__":
    main()
