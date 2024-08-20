#include <stdio.h>

int main()
{
    int num, n1, n2, aux, cont = 0;
    scanf("%d", &num);
    for (int j = 0; j < num; j++)
    {
        scanf("%d %d", &n1, &n2);
        cont = 0;
        if (n1 < n2)
        {
            aux = n1;
            n1 = n2;
            n2 = aux;
        }
        for (int i = n2 + 1; i < n1; i++)
        {
            if (i % 2 != 0)
            {
                cont += i;
            }
        }
        printf("%d\n", cont);
    }
    return 0;
}