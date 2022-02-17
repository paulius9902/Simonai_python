def func(list):
    vardai_u5 = list.copy()
    balses = 'AaĄaEeĘęĖėIiĮįYyOoUuŲųŪū'
    for i, s in enumerate(vardai_u5):
        if s[len(s)-1] in balses:
            vardai_u5[i] = s + ', studijuojanti FinTech'
        else:
            vardai_u5[i] = s + ', besimokantis Python'
    return  vardai_u5


if __name__ == '__main__':
    lt_raides= 'čšžąęėįųūČŠŽĄĘĖĮŲŪ'
    vardai1 = ['Augustas', 'Žilvinas', 'Česlovas', 'Ąžuolas', 'Mindaugas', 'Kęstutis']
    vardai2 = ['Lina', 'Živilė', 'Kamilė', 'Rasa', 'Jolita']
    vardai3 = ['Jonas', 'Petras']

    vardai = vardai1 + vardai2 + vardai3

    new_list = func(vardai)

    for s in new_list:
        for c in s:
            if c in lt_raides:
                print(s)
                break
