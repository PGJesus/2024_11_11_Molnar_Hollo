"""
1.2 Feladat
Fejleszd tovább úgy az előző programot, hogy a 3. név megadása után tájékoztassa a program a felhasználót, hogy már nincs lehetősége újabb adat bevitelére, írja ki az addig megadott neveket, és lépjen ki.
"""

nevek = []
def a():
    while True:
        if len(nevek) == 3:
            print("Háromnál többet nem adhatsz meg!")
            break
        nev = input("Adj meg egy keresztnevet: ")
        if nev == "":
            break
        nevek.append(nev)
    print(nevek)


def b():
    for i in range(1, 4):
        nev = input("Adj meg egy keresztnevet: ")
        if nev == "":
            break
        nevek.append(nev)
    print(nevek)



#a()
b()