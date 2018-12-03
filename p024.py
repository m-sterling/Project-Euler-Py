if __name__ == "__main__":
    from itertools import permutations as p

    l = sorted([i for i in range(10)])
    perms = p(l)
    n = "".join([str(i) for i in list(perms)[999999]])

    print(n)
