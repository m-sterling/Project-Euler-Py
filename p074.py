from math import factorial

if __name__ == "__main__":
    def fact_sum(n):
        total = 0
        for i in str(n):
            total += factorial(int(i))
        return total

    non_repeats = 0

    for i in range(1000000):
        chain = [i]
        n = i

        for j in range(60-1):
            n = fact_sum(n)
            if n in chain:
                break
            else:
                chain.append(n)
        else:
            non_repeats += 1

    print(non_repeats)
