#include <stdio.h>

int main()
{
    double c1 = 4, c2 = 4.5, c3 = 5, c4 = 2, c5 = 1.5, total;
    int cod, quant;
    scanf("%d %d", &cod, &quant);
    if (cod == 1)
    {
        total = c1 * quant;
    }
    else if (cod == 2)
    {
        total = c2 * quant;
    }
    else if (cod == 3)
    {
        total = c3 * quant;
    }
    else if (cod == 4)
    {
        total = c4 * quant;
    }
    else if (cod == 5)
    {
        total = c5 * quant;
    }
    printf("Total: R$ %.2lf\n", total);
    return 0;
}