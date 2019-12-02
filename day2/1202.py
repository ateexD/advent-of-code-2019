def compute_1(arr):
    n = len(arr)
    for i in range(0, n, 4):
        if arr[i] == 99:
            break
        else:
            x, y, z = arr[i + 1], arr[i + 2], arr[i + 3]
            if arr[i] == 1:
                arr[z] = arr[x] + arr[y]
            elif arr[i] == 2:
                arr[z] = arr[x] * arr[y]
    return arr[0]


def compute_2(arr):
    n = len(arr)
    for i in range(100):
        for j in range(100):
            arr[1], arr[2] = i, j
            if compute_1(arr.copy()) == 19690720:
                return i * 100 + j


if __name__ == '__main__':
    f = open('input.txt', 'r')
    arr_ = [int(x) for x in f.read().strip().split(',')]
    arr_[1], arr_[2] = 12, 2
    print(compute_1(arr_.copy()))
    print(compute_2(arr_.copy()))
    f.close()

