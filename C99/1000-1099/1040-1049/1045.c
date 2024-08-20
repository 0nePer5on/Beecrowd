#include <stdio.h>
#include <math.h>

int main()
{
    double n1, n2, n3, maior, sMaior, menor;
    scanf("%lf %lf %lf", &n1, &n2, &n3);
    if (n1 > 0 && n2 > 0 && n3 > 0)
    {
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
        if (maior >= sMaior + menor)
        {
            printf("NAO FORMA TRIANGULO\n");
        }
        else
        {
            if (pow(maior, 2) == pow(sMaior, 2) + pow(menor, 2))
            {
                printf("TRIANGULO RETANGULO\n");
            }
            if (pow(maior, 2) > pow(sMaior, 2) + pow(menor, 2))
            {
                printf("TRIANGULO OBTUSANGULO\n");
            }
            if (pow(maior, 2) < (pow(sMaior, 2) + pow(menor, 2)))
            {
                printf("TRIANGULO ACUTANGULO\n");
            }
            if (maior == sMaior && maior == menor)
            {
                printf("TRIANGULO EQUILATERO\n");
            }
            if ((maior == sMaior && maior != menor) || (maior != sMaior && maior == menor) || (sMaior == menor && sMaior != maior))
            {
                printf("TRIANGULO ISOSCELES\n");
            }
        }
    }
    return 0;
}