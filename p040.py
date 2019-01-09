if __name__ == "__main__":
    n = "." # offset indices by 1
    i = 1
    while len(n) - 1 < 1000000:
        n += str(i)
        i += 1
        
    print(int(n[1]) * int(n[10]) * int(n[100]) * int(n[1000]) * int(n[10000]) * int(n[100000]) * int(n[1000000]))
