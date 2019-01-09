if __name__ == "__main__":
    def has_same(a,b,c,d,e):
        al, bl, cl, dl, el = sorted(str(a)), sorted(str(b)), sorted(str(c)), sorted(str(d)), sorted(str(e))

        return al == bl and bl == cl and cl == dl and dl == el

    i = 1
    while True:
        a, b, c, d, e = 2*i, 3*i, 4*i, 5*i, 6*i
        if has_same(a, b, c, d, e):
            break
        else:
            i += 1

    print(i)
