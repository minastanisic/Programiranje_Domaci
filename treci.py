num = input("Unesite broj: ")
num = int(num)
sum = 1

for i in range(1, num+1):
    sum = sum*i

print("Faktorijal je: " + str(sum))