def time_sec():
    time = float(input("Unesite broj sekunda u danu: "))
    hr = time // 3600
    time %= 3600
    min = time // 60
    time %= 60
    sec = time
    print(" %d:%d:%d " % (hr, min, sec))


if __name__ == '__main__':
    time_sec()