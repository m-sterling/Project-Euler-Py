if __name__ == "__main__":
    def factorial(n):
        if n == 1:
            return 1
        return n * factorial(n-1)

    n = factorial(100)
    s, t = str(n), 0

    for c in s:
        t += int(c)

    print(t)
