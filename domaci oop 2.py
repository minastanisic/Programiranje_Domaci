import random


class Knjiga:

    def __init__(self, naslov, autor, zanr):
        self.isbn = str(random.randint(1, 100))
        self.naslov = naslov
        self.autor = autor
        self.zanr = zanr

        self.biblioteka = Biblioteka


class Biblioteka:

    def __init__(self, naziv_biblioteke):
        self.naziv = naziv_biblioteke
        self.knjige = []


biblioteka = Biblioteka("Gradska biblioteka")
biblioteka.knjige = [  {"Ime": "Ubistvo u Mesopotamiji", "Autor": "Agata Kristi", "Zanr": "roman", "ISBN": str(random.randint(1, 100))},
                     {"Ime": "Alhemicar", "Autor": "Paulo Koeljo", "Zanr": "roman", "ISBN": str(random.randint(1, 100))},
                     {"Ime": "Evenije Onjegin", "Autor": "Aleksandar Puskin", "Zanr": "roman", "ISBN": str(random.randint(1, 100))}  ]



def dodaj_knjigu():
    naslov = input("Naslov knjige: ")
    autor = input("Autor: ")
    zanr = input("Zanr: ")
    nova_knjiga = Knjiga(naslov, autor, zanr)
    biblioteka.knjige.append({"Naslov": nova_knjiga.naslov, "Autor": nova_knjiga.autor,"Zanr": nova_knjiga.zanr, "ISBN": nova_knjiga.isbn})


def podaci_knjiga():
    pretrazi_po_isbn = input("ISBN knjige: ")

    for knjiga in biblioteka.knjige:
        if pretrazi_po_isbn == knjiga["ISBN"]:
            print(knjiga)
            break
        else:
            print("Knjiga nije pronadjena")

def podaci_biblioteka():
    print("Ime biblioteke:", biblioteka.naziv)
    print("Knjige koje su dostupne: ", biblioteka.knjige)


if __name__ == '__main__':

    def meni():
        print("\n1. Dodavanje knjige")
        print("2. Podaci o biblioteci")
        print("3. Podaci o knjizi")
        print("x. Kraj")

    while True:
        meni()

        broj = input(" --- ")

        if broj == "1":
            dodaj_knjigu()
        if broj == "2":
            podaci_biblioteka()
        if broj == "3":
            podaci_knjiga()
        if broj == "x":

            break