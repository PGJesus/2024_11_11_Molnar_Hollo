"""
1.1 Feladat
A program tároljon egy listában színeket. Kérjen be a felhasználótól egy színt, és állapítsa meg, hogy a megadott szín már szerepel-e az adott listában. A vizsgálat eredményéről tájékoztassa a program a felhasználót, és írja ki egymás mellé vesszővel elválasztva a lista által tartalmazott színeket!"""

# ha a szín nem szerepel a listában, egészítsd ki a listát a zsínnel majd printeld is ki a listát

szinek = ['piros', 'zöld', 'kék', 'sárga', 'fekete', 'fehér']
szin = input("Adj egy színt! ")

if szin in szinek:
    print("Már van a listában ilyen szín.")
    print(szinek)
else:
    print(f"A {szin} szín nem szerepel a listában.")
    szinek.append(szin)
    print(szinek)

# töröld a megadott színt a listából

szinek.remove(szin)
print(szinek)