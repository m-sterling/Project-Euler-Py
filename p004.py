if __name__ == "__main__":
    largest = 0
    for a in range(100, 1000):
        for b in range(100, 1000):
            prod = a * b
            if prod > largest:
                prod_str = str(prod)
                prod_arr = list(prod_str)
                prod_rev = list(reversed(prod_arr))
                if prod_arr == prod_rev:
                    largest = prod
    print(largest)
