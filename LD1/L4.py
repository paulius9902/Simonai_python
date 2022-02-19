#funkcija su try ir except
def func(nums, num):
    try:
        sk = nums[num-1] #eilės numeris -1? iš sąrašo paima skaičių, kurio indeksas num-1
        return sk
    except IndexError:
        return "Įvestas blogas eilės numeris!"

#funkcija be try ir except
def func1(nums, num):
    if len(nums) >= num and num > 0: #indeksas turi būti mažesnis nei viso sąrašo ilgis
        sk = nums[num-1]
        return sk
    else:
        return "Įvestas blogas eilės numeris!"

sarasas1 = [1, 5, 0, -9, 3]
sarasas2 = [[1, 5], [0, -9, 3], [7, 2, 8, 20]]

res = func1(sarasas2, 0)
print(res)

#Išbandyta help funkcija
help(sarasas1)

#Pavyzdys
try:
    help(sarasas1.pop(10)) #ištrina 10 narį, bet jo nėra
except:
    print("Nerastas sąrašo elementas arba jo negalima ištrinti!")