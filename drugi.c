#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    FILE* dat = fopen ("Datoteka.txt", "w+");
    char str[20], c;
    int br=0, i;
    printf("Unesite string: ");
    scanf("%s", str);
    getchar();
    fprintf(dat, "%s", str);
    printf("Unesite karakter: ");
    scanf("%c", &c);
    fseek(dat,0,SEEK_SET);
    int duzina=strlen(str);
    for(i=0; i<duzina; i++){
        if (c == fgetc(dat)){
            br++;
        }
    }

    printf("Karakter se pojavljuje %d puta u unesenom stringu", br);


    return 0;
}


