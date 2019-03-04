if __name__ == "__main__":
    def calc_sum(num):
        s = 0
        for i in str(num):
            s += int(i)
        return s

    max_sum = 0
    for a in range(100):
        for b in range(100):
            max_sum = max(max_sum, calc_sum(a**b))

    print(max_sum)
