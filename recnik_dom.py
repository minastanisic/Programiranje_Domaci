lista = {}

def meni():
    print("-- MENI --")
    print("1 Unos ")
    print("2 Brisanje ")
    print("3 Izmena ")
    print("4 Ispis ")
    print("5 Kraj ")
    print("-----------------------------")

def unos():
  print("Unos: ")
  redni_broj = input(" Redni broj: ")
  ime = input(" Ime ")
  lista[redni_broj] = ime
  print(lista)
  
def brisanje():
  brisanje = input("Unesirte redni broj koji zelite da ibrisete:")
  lista.pop(brisanje)
  print(lista)
  
def izmena():
  redni_broj = input("Unesite broj koji zelite izmeniti: ")
  izmena = input("Novo ime: ")
  lista[redni_broj] = izmena
  print(lista)
  
def ispis():
  for redni_broj, ime in lista.items():
    print(redni_broj, ime)
    

if __name__ == '__main__':
  while True:
    meni()
    
    a = input("---")
    
    if a =='1':
      unos()
    elif a == '2':
      brisanje()
    elif a == '3':
      izmena()
    elif a == '4':
      ispis()
    elif a == "5":
      break
      
      