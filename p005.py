if __name__ == "__main__":
    dividend = 20
    while True:
        for divisor in range(1, 20+1):
            if not dividend % divisor == 0:
                break
        else:
            break
        dividend += 1
        continue
    print(dividend)
