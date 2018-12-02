if __name__ == "__main__":
    longest = 0
    for i in range(13, 1000000):
        n = i
        chain = 1
        while not n == 1:
            if n % 2 == 0:
                n /= 2
            else:
                n = 3*n + 1
            chain += 1
        if chain > longest:
            longest = chain
            longest_i = i
    print(longest_i)
