#include <stdio.h>

int main()
{
    int num, n, cont;
    scanf("%d", &num);
    for (int j = 0; j < num; j++)
    {
        scanf("%d", &n);
        cont = 0;
        for (int i = 1; i <= n; i++)
        {
            if (n % i == 0)
            {
                cont++;
            }
        }
        if (cont == 2)
        {
            printf("%d eh primo\n", n);
        }
        else
        {
            printf("%d nao eh primo\n", n);
        }
    }
    return 0;
}