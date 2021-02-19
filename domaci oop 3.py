
def meni():
    print("----------//-----------")
    print("1 Novi hotel\n"
          "2 Ispis hotela\n"
          "x Kraj")
    print("----------//-----------")

class hotel:
    def __init__(self, ime, adresa, grad):
        self.ime = ime
        self.adresa = adresa
        self.grad = grad
    def __str__(self):
        return f"Ime: {self.ime}" \
               f"Adresa: {self.adresa}" \
               f"Grad: {self.grad}"



lista_hotela = [
    {"Ime": "Hotel Moskva", "Broj zvezdica": "4", "Adresa": "Terazije 20", "Grad": "Beograd"},
    {"Ime": "Hotel Prime", "bBroj zvezdica": "4", "Adresa": "Radoslava Grujica 13", "Grad": "Beograd"},
    {"Ime": "Belgrade City Hotel", "Broj zvezdica": "4", "Adresa": "Savski trg 7", "Grad": "Beograd"},
    {"Ime": "Crown Plaza", "Broj zvezdica": "4", "Adresa": "Vladimira Popovica 10", "Grad": "Beograd"}]



class hotel1(hotel):
    def __init__(self, zvezdice):
        hotel1.__init__(self)
        self.zvezdice = zvezdice

    def novi_hotel(self):
        self.ime = input("Ime hotela: ")
        self.grad = input("Gde se nalazi hotel: ")
        self.zvezdice = input("Koliko zvezdica hotel ima: ")
        self.adresa = input("Na kojoj se adresi nalazi hotel: ")
        lista_hotela.append({"Ime": self.ime,
                             "Adresa": self.adresa,
                             "Broj zvezdica": self.zvezdice,
                             "Grad": self.grad})

    def __str__(self):
        return f"Ime: {self.ime}, Adresa: {self.adresa}, Broj zvezdca: {self.zvezdice}, Grad: {self.grad}"

if __name__ == '__main__':
    while True:
        meni()
        izbor = input("")

        if izbor == '1':
            Hotel = hotel1
            hotel1.novi_hotel(Hotel)
            print("Dodali ste hotel", end='\n')
        elif izbor == '2':
            i = 0
            for a in lista_hotela:
                print(lista_hotela[i], end='\n')
                i = i + 1
        elif izbor == 'x':
            print("Kraj")
            break
        else:
            print("Greska. Unesie ponovo")