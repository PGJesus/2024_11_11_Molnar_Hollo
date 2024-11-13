nyelvek = ['Pyhon', 'C', 'C++', 'Java', 'Python']
nyelvek2 = sorted(nyelvek)
print(nyelvek2)
print(nyelvek)

#sorba rendezi a listát
nyelvek.sort()
print(nyelvek)

#fordított sorba rendezi a listát
nyelvek.reverse()
print(nyelvek)




#az adott elem első előfordulásának indexe
print(nyelvek.index('C'))
print(nyelvek.index('C++'))

#az adott elem hányszor fordul elő
print(nyelvek.count('Python'))

#NEM listametódus, de így lehet eldönteni, hogy egy elemet tartalmaz- e a lista
print('C++' in nyelvek)
print('C+++' in nyelvek)

nev = "Hello"
print(nev.index("l"))