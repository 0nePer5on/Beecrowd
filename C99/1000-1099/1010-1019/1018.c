#include <stdio.h>

int main()
{
    int i, n, quant;
    int notas[7] = {100, 50, 20, 10, 5, 2, 1};
    scanf("%d", &n);
    printf("%d\n", n);
    for (i = 0; i < 7; i++)
    {
        if (n >= notas[i])
        {
            quant = n / notas[i];
            n %= notas[i];
            printf("%d nota(s) de R$ %d,00\n", quant, notas[i]);
        }
        else
        {
            printf("0 nota(s) de R$ %d,00\n", notas[i]);
        }
    }
    return 0;
}