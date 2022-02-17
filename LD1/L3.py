if __name__ == '__main__':
    while True:
        try:
            n = input("\nĮveskite skaičių: ")
            if int(n) < 0:
                break
            elif int(n) > 0:
                print(n)
        except ValueError:
            print("Įveskite skaičių!")
