if __name__ == "__main__":
    combos = []

    for a in range(2, 100+1):
        for b in range(2, 100+1):
            res = a ** b
            if not res in combos:
                combos.append(res)

    print(len(combos))
