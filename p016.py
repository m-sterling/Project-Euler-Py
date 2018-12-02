if __name__ == "__main__":
    sum = 0
    num = 2 ** 1000

    for c in str(num):
        sum += int(c)

    print(sum)
