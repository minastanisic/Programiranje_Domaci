#include <stdio.h>
#include <stdlib.h>

int funkcija(char* str, char* c){

    int suma=0;
    printf("Unesite string: ");
    gets(str);
    printf("Unesite karakter koji zelite: ");
    scanf("%c", &c);
    for(int i=0; str[i]!='\0'; i++){
        if(c==str[i])
            suma++;
    }

    printf("Karatker (%c) koji ste uneli pojavljuje se %d puta u stringu.", c, suma);
}

int main()
{
    char str[20];
    char c;
        funkcija(str, c);

    return 0;
}
