#include <stdio.h>

int main()
{
    double n1, n2, n3, valor;
    scanf("%lf %lf %lf", &n1, &n2, &n3);
    if (n1 + n2 > n3 && n1 + n3 > n2 && n2 + n3 > n1)
    {
        valor = n1 + n2 + n3;
        printf("Perimetro = %.1lf\n", valor);
    }
    else
    {
        valor = ((n1 + n2) * n3) / 2;
        printf("Area = %.1lf\n", valor);
    }
    return 0;
}