def find_duplicatchars(input_str):
    char_count = {}  # dictionary
    duplicates = []

    for i in input_str:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1

    for i, count in char_count.items():
        if count > 1:
            duplicates.append(i)
    return duplicates

input_string = "kiran vydhyam mai devi"
print(find_duplicatchars(input_string))
