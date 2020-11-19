def unos():
    ime = input("Unesite ime: ")
    lozinka = input("Unesite lozinku: ")
    file = open("fajl.txt", "a")
    file.write(ime)
    file.write("//")
    file.write(lozinka)
    print("Unos je uspesan")
    file.close()


if __name__ == '__main__':
    unos()