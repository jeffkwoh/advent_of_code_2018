def main():
    # open the file
    filename = "input.txt"
    file =  open(filename, "r")

    # initialise vars
    counter = 0
    s = set()
    foundDup = False

    # Keep looping if the a repeat freq is not found by EOF
    while not foundDup:
        for line in file:
            # logic for getting number
            number = int(line[1:])
            counter += number if line[0] == '+' else -number
            # logic for checking for dup.
            # Here we use a set to keep track of all seen numbers
            if counter not in s:
                s.add(counter)
            else:
                print(counter)
                foundDup = True
                break

        # reset file FP to 0 after done with reading the file
        file.seek(0)

    file.close()

if __name__ == "__main__":
    main()
