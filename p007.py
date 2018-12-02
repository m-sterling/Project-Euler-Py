if __name__ == "__main__":
    primes = []
    i = 1
    while not len(primes) == 10001:
        i += 1

        for n in range(2, i):
            if i % n == 0:
                break
        else:
            primes.append(i)
            continue

        continue

    print(primes[-1])
