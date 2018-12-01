if __name__ == "__main__":
    factors = []
    def factor(n):
        global factors
        for i in range(2, n+1):
            if n % i == 0:
                factors.append(i)
                factor(int(n/i))
                break

    factor(600851475143)
    print(factors)
    print(sorted(factors)[-1])
