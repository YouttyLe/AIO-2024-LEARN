def word_count(file_path):
    counter = {}
    with open(file_path, 'r') as f:
        data = f.read()
    data = data.lower()
    data = data.split()
    for word in data:
        counter[word] = counter.get(word, 0) + 1
    return counter


if __name__ == "__main__":
    file_path = 'D:\AIO-128-Study\AIO-2024-LEARN\Module1\WEEK_2_Data Structure _Exercise\P1_data.txt'
    print(word_count(file_path))
