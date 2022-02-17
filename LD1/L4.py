#funkcija su try ir except
def func(nums, num):
    try:
        sk = nums[num-1]
        return sk
    except IndexError:
        return "Įvestas blogas eilės numeris!"

#funkcija be try ir except
def func1(nums, num):
    if len(nums) >= num:
        sk = nums[num-1]
        return sk
    else:
        return "Įvestas blogas eilės numeris!"

sarasas1 = [1, 5, 0, -9, 3]
sarasas2 = [[1, 5], [0, -9, 3], [7, 2, 8, 20]]

res = func1(sarasas2, 4)

#Išbandyta help funkcija
#print(res)

#Pavyzdys
try:
    help(sarasas1.pop(10))
except:
    print("Nerastas sąrašo elementas arba jo negalima ištrinti!")