# Dvourozměrné pole
pole = [
    [1, 2, 3],
    [4, 105, 6],
    [7, 8, 9]
]

# Nebyl jsem si jistý jak jste to chtěla, šlo to udělat tak že bych prostě přidal nový řádek a sloupec do toho samotnýho pole ale takhle to je lepší si myslím. 

# Extra řádek
novy_radek = [10, 11, 12]
pole.append(novy_radek)

# Extra sloupec 
novy_sloupec = [13, 14, 15, 16]
for i in range(len(pole)):
    pole[i].append(novy_sloupec[i])

print(pole)
