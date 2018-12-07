def counter(input_str):
    count_dict = {}

    for char in input_str:
        if char not in count_dict:
            count_dict[char] = 1
        else:
            count_dict[char] += 1
    # Keeps track of counts of letters appearing exactly twice, and thrice.
    # [1, 3] -> one letter appeared twice, 3 appeared thrice.
    num_counter = [0,0];
    for k, v in count_dict.items():
        if v == 2:
            num_counter[0] += 1
        elif v == 3:
            num_counter[1] += 1
    return num_counter

def main():
    filename = "input.txt"
    file = open(filename, "r")

    appears_twice = 0
    appears_thrice = 0

    for line in file:
        num_counter = counter(line)
        appears_twice += 1 if num_counter[0] > 0 else 0
        appears_thrice += 1 if num_counter[1] > 0 else 0

    print(appears_twice * appears_thrice)

if __name__ == "__main__":
    main()
