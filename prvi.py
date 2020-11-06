months = []


def days_in_month():
    month = input("Unesite redni broj meseca: ")
    if month == '1' or month == '3' or month  == '5' or month  == '7' or month  == '8' or month  == '10' or month  == '12':
        print("Odabrani mesec ima 31 dan")
    elif month == '4' or month == '6' or month == '9' or month == '11':
        print("Odabrani mesec ima 30 dana")
    elif month == '2':
        print("Odabrani mesec ima 28, 29 dana")
    else:
        print("Odabrani mesec ne postoji")


if __name__ == '__main__':
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    days_in_month()