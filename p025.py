if __name__ == "__main__":
    def fib(a, b, i, limit):
        c = a + b
        i += 1
        l = len(str(c))
        if l == limit or i % 990 == 0: # Python can recurse up to 1000 times before throwing an error, so we can "restart" the recursion
            return b, c, i, limit
        return fib(b, c, i, limit)

    a, b, i = 1, 1, 2
    limit = 1000
    while not len(str(a+b)) == limit:
        a, b, i, limit = fib(a, b, i, limit)
    print(i)
