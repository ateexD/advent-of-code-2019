def compute_1(val):
    return int(val / 3) - 2


def compute_2(val):
    temp = int(val / 3) - 2
    if temp < 0:
        return 0
    return temp + compute_2(temp)


if __name__ == "__main__":
    f = open('input.txt', 'r')
    vals = f.read().strip().split('\n')

    ans_1 = sum((compute_1(int(val)) for val in vals))
    ans_2 = sum((compute_2(int(val)) for val in vals))

    print(ans_1, ans_2)
    f.close()

