def func(start, end, step):
    cnt=0 #nuo čia pradeda skaičiuoti iteracijas? Pirmas testinimas?
    for i in range(start, end, step):
        if (i % 2) == 0:
            odd_even = "lyginis" # odd_even yra kintamasis
        else:
            odd_even = "nelyginis"

        if (i % 7) == 0:
            div = "be liekanos" #tas pats kaip ir su odd_even
        else:
            div = "su liekana " + str(i % 7) #str kad atspausdintų liekaną, skausdina skaitinę reikšmę

        print("Iteracijos nr: {}, skaitliuko reikšmė: {} yra {} skaičius, kuris dalinasi iš 7 {}".format(cnt, i, odd_even, div))
        cnt+=1 #pradeda antrą iteraciją su +1? cnt=cnt+1


func(20, 60, 3)
print('------------------------------------------------------------------------') #atskyrimas tarp funkcijų
func(100, 200, 5)
