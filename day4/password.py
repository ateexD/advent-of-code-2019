import itertools as it


def check_1(num):
    num = [int(x) for x in str(num)]
    double = any([num[i] == num[i + 1] for i in range(5)])
    inc = num == sorted(num)
    return double and inc


def check_2(num):
    num = [int(x) for x in str(num)]
    inc = num == sorted(num)
    if not inc:
        return False

    for _, grp in it.groupby(num):
        if len(list(grp)) == 2:
            return True
    return False


if __name__ == "__main__":
    ans_1, ans_2 = 0, 0
    for num in range(402328, 864247 + 1):
        if check_1(num):
            ans_1 += 1
        if check_2(num):
            ans_2 += 1
    print(ans_1, ans_2)

