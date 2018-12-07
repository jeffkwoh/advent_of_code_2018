# assumes strs are the same length
def chk_diff(str_a, str_b, target_diff = 1):
    return len([1 for a, b in zip(str_a, str_b) if a != b]) == target_diff

def get_common_str(str_a, str_b):
    return ''.join([a for a, b in zip(str_a, str_b) if a == b])

def main():
    filename = "input.txt"
    file = open(filename, "r")
    list_of_ids = file.readlines();
    diff_only_one = [(x, y) for x in list_of_ids for y in list_of_ids if chk_diff(x, y)]
    result = [get_common_str(x, y) for x, y in diff_only_one]
    print(result)

if __name__ == "__main__":
    main()
