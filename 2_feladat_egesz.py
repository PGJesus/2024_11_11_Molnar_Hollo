"""2.1 Feladat
Készíts egy programot, amely a felhasználótól kis "a" betűvel kezdődő szavakat kér be és
ezeket tárolja. Ha a felhasználó nem "a" betűvel kezdődő szót ad meg, akkor azt hagyja figyelmen
kívül és ne tárolja. A bekérés egészen addig folytatódjon, amíg a felhasználó ENTER-t nem üt
(nem ad meg újabb nevet a bekérésnél)! A program a bekért neveket írja ki a képernyőre!

A program tájékoztatássa a felhasználót a működéséről, és az elvárt adatokról!"""

def feladat():

    szavak = []

    print("Adj meg olyan szavakat, amelyek 'a' betűvel kezdődnek!")
    print("A nem 'a' betűvel kezdődő szavakat a rendszer nem fogja tárolni.")
    print("Ha kész vagy, nyomj enter billenytűt a program befejezéséhez!")

    while True:
        szo = input("Adj egy szót: ")
        
        if szo == "":
            break
        
        if szo.lower().startswith('a'):
            szavak.append(szo)
        else:
            print(f"A '{szo}' nem 'a' betűvel kezdődik, adjon meg egy újabb szót!")

    print("A tárolt szavak:")
    for szo in szavak:
        print(szo)


"""2.2 Feladat
Alakítsd át úgy az előző porgramot, hogy az ne csak kis, hanem a nagy "A" betűvel kezdődő
szavakat is elfogadja."""

def feladat_2():

    szavak = []

    print("Szervusz! Adj meg olyan szavakat, amelyek 'a' betűvel kezdődnek!")
    print("A nem 'a' betűvel kezdődő szavakat a rendszer nem fogja tárolni.")
    print("Ha kész vagy, nyomj ENTER-t a program befejezéséhez!")

    while True:
        szo = input("Adj meg egy szót: ")

        if szo == "":
            break
        
        if szo.lower().startswith('a'):
            szavak.append(szo)
        else:
            print(f"A '{szo}' nem 'a' betűvel kezdődik, adjon meg egy újabb szót!")

    print("A tárolt szavak:")
    for szo in szavak:
        print(szo)

feladat()
feladat_2()
