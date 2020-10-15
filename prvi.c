#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *dat;
    char str[20];
    dat=fopen("Datoteka.txt","w+");

    if(dat==NULL){
        printf("Greska.");
        return 1;
    }
    printf("Unesite ime, prezime i broj u dnevniku: ");
    fgets(str,sizeof(str),stdin);
    fprintf(dat,"%s",str);
    fclose(dat);
    return 0;
}
