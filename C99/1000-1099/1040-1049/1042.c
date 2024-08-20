#include <stdio.h>

int main()
{
    int n1, n2, n3, maior, sMaior, menor;
    scanf("%d %d %d", &n1, &n2, &n3);
    maior = n1;
    sMaior = n2;
    menor = n3;
    if (sMaior < n3)
    {
        sMaior = n3;
        menor = n2;
    }

    if (maior < n2)
    {
        maior = n2;
        sMaior = n1;
        menor = n3;
        if (sMaior < n3)
        {
            sMaior = n3;
            menor = n1;
        }
    }

    if (maior < n3)
    {
        maior = n3;
        sMaior = n1;
        menor = n2;
        if (sMaior < n2)
        {
            sMaior = n2;
            menor = n1;
        }
    }
    printf("%d\n%d\n%d\n\n", menor, sMaior, maior);
    printf("%d\n%d\n%d\n", n1, n2, n3);
    return 0;
}