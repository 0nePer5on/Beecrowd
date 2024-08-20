#include <stdio.h>

int main()
{
    int i, j, quant, vez = 0;
    double n;
    double din[12] = {100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01};
    scanf("%lf", &n);
    n += 0.001;
    printf("NOTAS:\n");
    for (i = 0; i < 12; i++)
    {
        j = 0;
        quant = 0;
        while (j == 0)
        {
            if (n >= din[i])
            {
                n -= din[i];
                quant++;
            }
            else
            {
                j++;
            }
        }
        if (i <= 5)
        {
            printf("%d nota(s) de R$ %.2lf\n", quant, din[i]);
        }
        else
        {
            if (vez == 0)
            {
                printf("MOEDAS:\n");
                vez++;
            }
            printf("%d moeda(s) de R$ %.2lf\n", quant, din[i]);
        }
    }
    return 0;
}