def func(num):
    res = False
    if i > 0:
        res = pow(i, 2)
    elif i < 0:
        res = pow(i, 3)
    elif i == 0:
        res = 0
    print(res)
    return res


if __name__ == '__main__':
    skaiciai3 = [5, -8, 3, 0, 9, -2, 0, 6, -9, 10]
    for i in skaiciai3:
        func(i)
