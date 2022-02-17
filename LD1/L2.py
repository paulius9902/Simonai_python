def func(start, end, step):
    cnt=0
    for i in range(start, end, step):
        if (i % 2) == 0:
            odd_even = "lyginis"
        else:
            odd_even = "nelyginis"

        if (i % 7) == 0:
            div = "be liekanos"
        else:
            div = "su liekana " + str(i % 7)

        print("Iteracijos nr: {}, skaitliuko reikšmė: {} yra {} skaičius, kuris dalinasi iš 7 {}".format(cnt, i, odd_even, div))
        cnt+=1

if __name__ == '__main__':
    func(20, 60, 3)
    func(100, 200, 5)
