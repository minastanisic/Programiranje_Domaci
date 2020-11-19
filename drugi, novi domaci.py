def spajanje():
    str1 = input("Unesite prvi string: ")
    str2 = input("Unesite drugi string: ")
    string_prva_tri_karaktera = str1[0:3]
    string_poslednja_tri_karaktera = str2[-3:]
    str = string_prva_tri_karaktera + string_prva_tri_karaktera + string_poslednja_tri_karaktera 
    print(str)

if __name__ == '__main__':
    spajanje()