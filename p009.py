if __name__ == "__main__":
    import math, sys
    for a in range(1000):
        for b in range(a+1, 1000):
            for c in range(b+1, 1000):
                if a < b and b < c and math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2) and a + b + c == 1000:
                    print(a*b*c)
                    sys.exit(0)