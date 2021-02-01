class krug():

    def __init__(self, r):
        self.poluprecnik = r

    def povrsina(self):
        return self.poluprecnik ** 2 * 3.14

    def obim(self):
        return 2 * self.poluprecnik * 3.14

poluprecnik = float(input("Unesite poluprecnik kruga: "))
NoviKrug = krug(poluprecnik)
print("Povrsina kruga je: ")
print(NoviKrug.povrsina())
print("Obim kruga je: ")
print(NoviKrug.obim())

class pravougaonik():

    def __init__(self, duzina_stranice_pravougaonika, sirina_stranice_pravougaonika):
        self.length = duzina_stranice_pravougaonika
        self.width  = sirina_stranice_pravougaonika

    def povrsina_pravougaonika(self):
        return self.length*self.width

    def obim_pravougaonika(self):
        return self.length+self.length+self.width+self.width

duzina_stranice_pravougaonika = float(input("Unesite duzinu pravougaonika: "))
sirina_stranice_pravougaonika = float(input("Unesite sirinu pravougaonika: "))

NoviPravougaonik = pravougaonik(duzina_stranice_pravougaonika, sirina_stranice_pravougaonika)
print("Povrsina pravougaonika je: ")
print(NoviPravougaonik.povrsina_pravougaonika())
print("Obim pravougaonika je: ")
print(NoviPravougaonik.obim_pravougaonika())

class kvadrat():

    def __init__(self, stranica_kvadrata):
        self.stranica_kvadrata = stranica_kvadrata

    def povrsina_kvadrata(self):
        return self.stranica_kvadrata*self.stranica_kvadrata

    def obim_kvadrata(self):
        return self.stranica_kvadrata*4

stranica_kvadrata = float(input("Unesite duzinu stranice kvadrata: "))

NoviKvadrat = kvadrat(stranica_kvadrata)
print("Povrsina kvadrata je: ")
print(NoviKvadrat.povrsina_kvadrata())
print("Obim kvadrata je: ")
print(NoviKvadrat.obim_kvadrata())