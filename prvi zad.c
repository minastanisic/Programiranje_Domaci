#include <stdio.h>
#include <stdlib.h>

int main()
{

    double mat[50][50], transponovana[50][50];
    int t, q, i, j;
    printf("Unesite broj redova i kolona kvadratne matrice: \n");
    do{
        scanf("%d %d", &t, &q);
    }
    while(t!=q);

    printf("Unesite elemente matrice: \n");
    for(i=0; i<t; i++)
        for(j=0; j<q; j++){
            printf("Unesite element mat[%d][%d]: ", i+1, j+1);
            scanf("%lf", &mat[i][j]);
        }

    printf("Uneta matrica je: \n");
    for(i=0; i<t; i++)
        for(j=0; j<q; j++){
            printf("%.1lf  ", mat[i][j]);
            if(j==t-1)
                printf("\n");
        }

    for(i=0; i<t; i++)
        for(j=0; j<q; j++){
            transponovana[j][i]=mat[i][j];
        }

    printf("Transponovana matrica je:\n");
    for(i=0; i<t; i++)
        for(j=0; j<q; j++){
            printf("%.1lf  ", transponovana[i][j]);
            if(j==t-1)
                printf("\n");
        }

    return 0;
}

