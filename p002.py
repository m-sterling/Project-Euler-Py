if __name__ == "__main__":
    sum = 2 # start with "1, 2"
    def fib(a, b, max):
        global sum
        c = a + b
        # print(c)
        if c < max:
            if c % 2 == 0:
                sum += c
            fib(b, c, max)
    fib(1, 2, 4000000)
    print(sum)
