import locale
locale.setlocale(locale.LC_ALL, '')

vardai1 = ['Augustas', 'Žilvinas', 'Česlovas', 'Ąžuolas', 'Mindaugas', 'Kęstutis']
vardai2 = ['Lina', 'Živilė', 'Kamilė', 'Rasa', 'Jolita']
vardai3 = ['Jonas', 'Petras']

print('Nesurikiuotas sąrašas: ')
joinedlist = vardai1 + vardai2 + vardai3
print(joinedlist)
print()

print('Surikiuotas sąrašas: ')
sortedlist = sorted(joinedlist, key=locale.strxfrm)
print(sortedlist)
print()

print("Ilgis: {}, pirmas elementas: {}, paskutinis elementas: {}, sąrašas: {}".format(len(sortedlist), sortedlist[0], sortedlist[len(sortedlist)-1], sortedlist))
