#include <stdio.h>
#include <stdlib.h>

int main () {

char c;
FILE *f1=fopen ("dat1.txt", "w+");
FILE *f2=fopen ("dat2.txt", "w+");
FILE *f=fopen("dat3.txt", "w+");

if(f1 == NULL || f2 == NULL){
getch();
exit(0);
}

if (f ==NULL){
exit(0);
}

while((c=fgetc(f1)) != EOF)
    fputc(c, f);

while((c=fgetc(f2)) != EOF)
    fputc(c, f);

printf("Fajlovi su spojeni.");

fclose(f1);
fclose(f2);
fclose(f);
getch();



return 0;

}


