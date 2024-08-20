#include <stdio.h>

int main()
{
    int num, a = 0, g = 0, d = 0, conf = 0;
    while (conf == 0)
    {
        scanf("%d", &num);
        if (num == 1)
        {
            a++;
        }
        else if (num == 2)
        {
            g++;
        }
        else if (num == 3)
        {
            d++;
        }
        else if (num == 4)
        {
            conf++;
        }
    }
    printf("MUITO OBRIGADO\n");
    printf("Alcool: %d\n", a);
    printf("Gasolina: %d\n", g);
    printf("Diesel: %d\n", d);
    return 0;
}