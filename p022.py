if __name__ == "__main__":
    file = open("inputs/p022_names.txt")
    src = file.read()
    arr = src.split(',')
    arr = [name[1:-1] for name in arr] # get rid of quotes
    arr.sort()                         # alphabetize

    total, i = 0, 0

    while not i == len(arr):
        name = arr[i]

        letter_val = 0
        for char in name:
            letter_val += ord(char) - ord('A') + 1

        total += (i+1) * letter_val

        i += 1

    print(total)
