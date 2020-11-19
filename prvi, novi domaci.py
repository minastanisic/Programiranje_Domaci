def ispis(ime):  
    if(len(ime) == 0): 
        return
    print(ime[0].upper()), 
    for i in range(1, len(ime) - 1): 
        if (ime[i] == ' '): 
            print (ime[i + 1].upper()), 
  
def main(): 
    ime = input("Unesite ime: ")
    ispis(ime) 
  
if __name__=="__main__": 
    main()  