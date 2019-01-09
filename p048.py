if __name__ == "__main__":
    t = 0
    for i in range(1, 10+1):
        t += i ** i

    print(str(t)[-10:])
