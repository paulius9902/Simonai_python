def func(nums, num):
    arr = []
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            arr.append(nums[i][j])
    try:
        sk = arr[num-1]
        return sk
    except IndexError:
        return "Įvestas blogas eilės numeris!"

sarasas1 = [1, 5, 0, -9, 3]
sarasas2 = [[1, 5], [0, -9, 3], [7, 2, 8, 20]]

res = func(sarasas1, 3)
print(res)