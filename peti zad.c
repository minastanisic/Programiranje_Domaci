#include <stdio.h>
#include <stdlib.h>

int main()
{

    int niz[100];
    int i, duzina;
    printf("Unesite duzinu niza: ");
    scanf("%d", &duzina);

    for(i=0; i<duzina; i++){

        printf("Unesite %d. element niza: \n", i+1);
        scanf("%d", niz+i);
    }

    for(i=0; i<duzina; i++){

        if(*(niz+i)%3==0){
            printf("%d \n", *(niz+i));
        }
    }


    return 0;
}
