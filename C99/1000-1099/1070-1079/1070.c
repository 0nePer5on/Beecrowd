#include <stdio.h>

int main()
{
    int n, conf = 0, i = 1, cont = 0;
    scanf("%d", &n);
    if (n % 2 == 0)
    {
        while (conf == 0)
        {
            if (i % 2 != 0)
            {
                printf("%d\n", n + i);
                cont++;
                if (cont == 6)
                {
                    conf++;
                }
            }
            i++;
        }
    }
    else
    {
        i = 0;
        while (conf == 0)
        {
            if (i % 2 == 0)
            {
                printf("%d\n", n + i);
                cont++;
                if (cont == 6)
                {
                    conf++;
                }
            }
            i++;
        }
    }
    return 0;
}