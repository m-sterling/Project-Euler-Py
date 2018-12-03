if __name__ == "__main__":
    def d(n):
        sum = 0
        for i in range(1, n):
            if n%i == 0:
                sum += i
        return sum

    amicable = []
    for i in range(1, 10000):
        if not i in amicable:
            n = d(i)
            if not n == i and d(n) == i:
                amicable.extend([i, n])

    sum = 0
    for i in amicable:
        sum += i

    print(sum)
