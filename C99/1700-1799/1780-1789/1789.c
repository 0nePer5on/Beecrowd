#include <stdio.h>

int main()
{
    int num, maior, n;
    while (scanf("%d", &num) != EOF)
    {
        scanf("%d", &n);
        maior = n;
        for (int i = 0; i < num - 1; i++)
        {
            scanf("%d", &n);
            if (maior < n)
            {
                maior = n;
            }
        }
        if (maior < 10)
        {
            printf("1\n");
        }
        else if (maior >= 10 && maior < 20)
        {
            printf("2\n");
        }
        else
        {
            printf("3\n");
        }
    }
    return 0;
}