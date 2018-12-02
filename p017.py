if __name__ == "__main__":
    nums_ones, nums_tens = {
        '0': '',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
    }, {
        '0':  '',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen',
        '2':  'twenty',
        '3':  'thirty',
        '4':  'forty',
        '5':  'fifty',
        '6':  'sixty',
        '7':  'seventy',
        '8':  'eighty',
        '9':  'ninety'
    }

    total = 0
    for i in range(1, 1000+1): # [1, 1000], so +1
        s, n = str(i), ""
        r = list(reversed(list(s)))
        if len(s) == 4: # 1000
            n = "one thousand"
        elif len(s) == 3: # xxx
            n += nums_ones[r[2]] + " hundred" # hundreds
            if not int(s[1:]) == 0: # not an even n-hundred
                n += " and "
            s = s[1:]

        if len(s) == 2: # xx
            if int(s) in range(10, 20): # 10-19
                n += nums_tens[s]
            else:
                n += nums_tens[r[1]] + " "
                n += nums_ones[r[0]]
        elif len(s) == 1: # x
            n += nums_ones[r[0]]

        n = "".join(n.split())
        total += len(n)
    print(total)
