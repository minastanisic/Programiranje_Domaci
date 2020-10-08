#include <stdio.h>
#include <stdlib.h>

void unos(int* mat1, int t, int q)
{
    int i, j;
    printf("Unesite elemente matrice:\n");
    for(i=0; i<t; i++)
        for(j=0; j<q; j++){
            printf("Unesite element mat1[%d][%d]: ", i+1, j+1);
            scanf("%d", mat1+i*q+j);
        }
}

void zbir(int* mat1, int* mat2, int* suma, int t, int q)
{
    int i, j;
    for(i=0; i<t; i++)
        for(j=0; j<q; j++){
           *(suma+i*q+j)=*(mat1+i*q+j)+*(mat2+i*q+j);
        }
}

void ispis(int* suma, int t, int q)
{
    int i, j;
    printf("Zbir matrica: \n");
    for(i=0; i<t; i++)
        for(j=0; j<q; j++){
            printf("%d  ", *(suma+i*q+j));
            if(j==q-1){
                printf("\n\n");
            }
        }
}

int main()
{
    int t, q, mat1[100][100], mat2[100][100], suma[100][100], i, j;
    printf("Unesite broj redova: ");
    scanf("%d", &q);
    printf("Unesite broj kolona: ");
    scanf("%d", &t);
    unos(mat1, t, q);
    unos(mat2, t, q);
    zbir(mat1, mat2, suma, t, q);
    ispis(suma, t, q);
    return 0;
}
