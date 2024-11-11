honapok = ['január', 'február', 'március', 'április','május']

print(honapok)

# lista hossza: len()
print(len(honapok))

# 0.index elem
print(honapok[0])

# 1.index elem
print(honapok[1])

# üres lista létrehozása:
szamok = []
print(szamok)
# elem hozzáadása
for i in range (1, 11):
    szamok.append(i)            # append-del hozzáadtunk elemeket
print(szamok[2])
print(szamok[9])
# túlindexelés -            IndexError :list index out of range
# print(szamok[10])

# utolsó elem megadása - hátulró az első elem
print(szamok[-1])
print(szamok[-2])