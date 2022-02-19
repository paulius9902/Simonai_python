def func(num):
    if type(num) == int or type(num) == float:  # kad išvengti raidinių reikšmių?
        if i > 0:
            res = pow(i, 2)  # tas pats kas ** (kėlimas laipsniu)
        elif i < 0:
            res = pow(i, 3)
        elif i == 0:
            res = i
        return res
    else:
        return False


skaiciai3 = [5, -8, 3, 0, 9, -2, 0, 6, -9, 10]
for i in skaiciai3:
    res = func(i)
    print(res)

# def func(num):
# if i > 0:
# res = i**2
# elif i < 0:
# res = i**3
# elif i == 0:
# res = 0
# return res

# skaiciai3 = [5, -8, 3, 0, 9, -2, 0, 6, -9, 10]
# for i in skaiciai3:
# res = func(i)
# print(res)
