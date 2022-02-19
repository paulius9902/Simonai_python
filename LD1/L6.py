def func(vardai):
    vardai_u5 = vardai.copy()
    balses = 'AaĄaEeĘęĖėIiĮįYyOoUuŲųŪū'
    for i, s in enumerate(vardai_u5): #kas tas i ir s? i indeksas, s - vardas
        if s[len(s)-1] in balses: #patikrina ar vardo paskutinė raidė yra balsė
            vardai_u5[i] = s + ', studijuojanti FinTech' #pakeičia sąrašo narį pagal indeksą
        else:
            vardai_u5[i] = s + ', besimokantis Python'
    return vardai_u5


lt_raides = 'čšžąęėįųūČŠŽĄĘĖĮŲŪ'
vardai1 = ['Augustas', 'Žilvinas', 'Česlovas', 'Ąžuolas', 'Mindaugas', 'Kęstutis']
vardai2 = ['Lina', 'Živilė', 'Kamilė', 'Rasa', 'Jolita']
vardai3 = ['Jonas', 'Petras']

vardai = vardai1 + vardai2 + vardai3

new_list = func(vardai)

for s in new_list:  # c raidės varduose
    for c in s:
        if c in lt_raides:
            print(s)
            break