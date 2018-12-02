if __name__ == "__main__":
    # use sieve of Eratosthenes https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    sum = 0
    l = [True]*2000000
    for i in range(2, len(l)):
        if l[i]:
            for j in range(2*i, len(l), i):
                l[j] = False
    for i in range(2, len(l)):
        if l[i]:
            sum += i
    print(sum)
