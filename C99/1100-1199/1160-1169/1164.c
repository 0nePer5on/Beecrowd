#include <stdio.h>

int main()
{
    int j, num, n1, conf, cont;
    scanf("%d", &num);
    for (int i = 0; i < num; i++)
    {
        scanf("%d", &n1);
        j = 1;
        conf = 0;
        cont = 0;
        while (conf == 0)
        {
            cont += j;
            j++;
            if (cont >= n1)
            {
                conf++;
            }
        }
        if (n1 == 1)
        {
            printf("1 nao eh perfeito\n");
        }
        else if (cont == n1)
        {
            printf("%d eh perfeito\n", n1);
        }
        else
        {
            printf("%d nao eh perfeito\n", n1);
        }
    }
    return 0;
}