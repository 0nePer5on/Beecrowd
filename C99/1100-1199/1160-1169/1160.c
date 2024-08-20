#include <stdio.h>

int main()
{
    int num, n1, n2, cont;
    double n3, n4;
    scanf("%d", &num);
    for (int i = 0; i < num; i++)
    {
        scanf("%d %d %lf %lf", &n1, &n2, &n3, &n4);
        cont = 0;
        while (n1 <= n2)
        {
            n1 += n1 * (n3 / 100);
            n2 += n2 * (n4 / 100);
            cont++;
            if (cont > 100)
            {
                n1 = n2 + 1;
            }
        }
        if (cont <= 100)
        {
            printf("%d anos.\n", cont);
        }
        else
        {
            printf("Mais de 1 seculo.\n");
        }
    }
    return 0;
}