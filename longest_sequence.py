def get_sequence(string):
    longest_sequence = ""
    current_sequence = ""
    index = 0

    while index < len(string):
        curr_str = string[index]

        if index > 0 and curr_str == string[index - 1]:
            current_sequence += curr_str
        elif index < len(string) - 1 and curr_str == string[index+1]:
            if curr_str != string[index - 1]:
                current_sequence = ""
            current_sequence += curr_str

        if len(current_sequence) > len(longest_sequence):
            longest_sequence = current_sequence
        index += 1

    return longest_sequence


print(get_sequence("11000335590900000"))
