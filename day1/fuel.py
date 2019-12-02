def compute_1(val):
    return int(val / 3) - 2

def compute_2(val):
    temp = int(val / 3) - 2
    if temp < 0:
        return 0
    return  temp + compute_2(temp)


if __name__ == "__main__":
    f = open('input.txt', 'r')
    vals = f.read().split('\n')
    ans_1 = 0
    ans_2 = 0

    try:
        for val in vals:
            ans_1 += compute_1(int(val))
            ans_2 += compute_2(int(val))
    except:
        pass

    print(ans_1, ans_2)
    f.close()
