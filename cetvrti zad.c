#include <stdio.h>
#include <stdlib.h>

int main()
{

    int niz[100], duzina, *max, i;
    printf("Unesite duzinu niza: ");
    scanf("%d", &duzina);

    for(i=0; i<duzina; i++){

        printf("Unesite %d. element niza: \n", i+1);
        scanf("%d", niz+i);
    }

    max=niz;
    *max=*niz;

    for(i=1; i<duzina; i++){

        if(*(niz+i)>*max){

            *max=*(niz+i);
        }
    }

    printf("Najveci element niza je %d", *max);


    return 0;
}
