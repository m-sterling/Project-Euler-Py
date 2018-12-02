if __name__ == "__main__":
    sum_of_sq, sq_of_sum = 0, 0

    for i in range(1, 100+1):
        sum_of_sq += (i*i)
        sq_of_sum += i

    sq_of_sum *= sq_of_sum
    print(sq_of_sum - sum_of_sq)
