if __name__ == "__main__":
    def is_circular_prime(n):
        if not primes[n]:
            return False

        def rotate(s):
            return s[1:] + s[0]

        pr = [n]
        s = str(n)
        r = rotate(s)
        while not r == s:
            if not primes[int(r)]:
                return False
            else:
                pr.append(int(r))
                r = rotate(r)
        return pr

    # use sieve of Eratosthenes from p10 https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    sum = 0
    primes = [True]*1000000
    for i in range(2, len(primes)):
        if primes[i]:
            for j in range(2*i, len(primes), i):
                primes[j] = False

    pr = []
    for i in range(2, 1000000):
        if primes[i] and not i in pr:
            circ = is_circular_prime(i)
            if circ:
                pr.extend(circ)

    print(len(pr))
