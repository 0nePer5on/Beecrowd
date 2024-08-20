#include <stdio.h>

int main()
{
    double num, n1, n2;
    int conf = 0, cont = 0, quant = 0, val = 0, escolha;
    while (quant == 0)
    {
        conf = 0;
        val = 0;
        cont = 0;
        while (conf == 0)
        {
            scanf("%lf", &num);
            if (num >= 0 && num <= 10)
            {
                if (cont == 0)
                {
                    n1 = num;
                    cont++;
                }
                else
                {
                    n2 = num;
                    conf++;
                }
            }
            else
            {
                printf("nota invalida\n");
            }
        }
        printf("media = %.2lf\n", (n1 + n2) / 2);
        while (val == 0)
        {
            printf("novo calculo (1-sim 2-nao)\n");
            scanf("%d", &escolha);
            if (escolha == 2)
            {
                quant++;
                val++;
            }
            else if (escolha == 1)
            {
                val++;
            }
        }
    }
    return 0;
}