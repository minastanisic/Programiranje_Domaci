def ispis():
    file = open("fajl.txt", "r")
    for line in file.readlines():
        user = line.split("|")
        ime = user[0]
        lozinka = user[1]
        print("ime: " + ime)
        print("lozinka: " + lozinka)
    file.close()


if __name__ == '__main__':
    ispis()