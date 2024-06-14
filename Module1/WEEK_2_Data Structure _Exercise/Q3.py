def count_word(file_path):
    word_count_dict = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            words = line.lower().split()
            for word in words:
                if word in word_count_dict:
                    word_count_dict[word] += 1
                else:
                    word_count_dict[word] = 1

    return word_count_dict


def main():
    file_path = 'P1_data.txt'
    print(count_word(file_path))


if __name__ == '__main__':
    main()
