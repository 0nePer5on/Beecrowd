#include <stdio.h>

int main()
{
    int n, impar[5], par[5], contP = 0, contI = 0;
    for (int i = 0; i < 15; i++)
    {
        scanf("%d", &n);
        if (n % 2 == 0)
        {
            par[contP] = n;
            if (contP == 4)
            {
                for (int j = 0; j < 5; j++)
                {
                    printf("par[%d] = %d\n", j, par[j]);
                }
                contP = 0;
            }
            else
            {
                contP++;
            }
        }
        else
        {
            impar[contI] = n;
            if (contI == 4)
            {
                for (int j = 0; j < 5; j++)
                {
                    printf("impar[%d] = %d\n", j, impar[j]);
                }
                contI = 0;
            }
            else
            {
                contI++;
            }
        }
    }
    if (contI != 0 && contP != 0)
    {
        for (int i = 0; i < contI; i++)
        {
            printf("impar[%d] = %d\n", i, impar[i]);
        }
        for (int i = 0; i < contP; i++)
        {
            printf("par[%d] = %d\n", i, par[i]);
        }
    }

    return 0;
}