if __name__ == "__main__":
    def palindrome(s):
        return s == s[::-1]

    sum = 0
    for i in range(1000000):
        b = "{0:b}".format(i)
        if palindrome(str(i)) and palindrome(b):
            sum += i

    print(sum)
