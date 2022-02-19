while True:
    try:
        n = input("\nĮveskite skaičių: ")
        if int(n) < 0:
            break #sustabdo ciklą, vykdo toliau, kas yra už for/while (po ciklu)
        elif int(n) > 0: #elif tikrino nurodytą sąlygą n>0, jei true, vykdo žemiau pateitą veiksmą (print). Jei netinka if, pereina elif, jei netinka abi ir nėra nurodyta kaip elgtis, grįžta prie while
            print(n)
    except ValueError:
        print("Neteisingai įvestas skaičius!")
