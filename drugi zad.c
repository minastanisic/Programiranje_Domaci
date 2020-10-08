#include <stdio.h>
#include <string.h>
#include <stdlib.h>


//nisam sigurna da li ste pod jednaki mislili isti u sastavu ili iste duzine ali
//ako treba iste duzine samo bih stavila if(strlen(str1)== strlen(str2)) i obrisala 13. liniju
//i kod bi radio isto samo za za duzinu stringa.


int jednaki(char* str1, char* str2){

    strcmp(str1, str2);

    if(strcmp(str1, str2)==0){
        printf("Stringovi su isti.");
    }

    else{
        printf("Stringovi su razliciti.");
    }

}

int main()
{

    char str1[20];
    char str2[20];


    printf("Unesite prvi string: ");

    gets(str1);

    printf("Unesite drugi string: ");

    gets(str2);

    jednaki(str1, str2);


    return 0;
}
