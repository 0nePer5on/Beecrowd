#include <stdio.h>

int main()
{
    int n, num;
    scanf("%d", &n);
    if (n < 10000)
    {
        for (int i = 0; i < n; i++)
        {
            scanf("%d", &num);
            if (num == 0)
            {
                printf("NULL\n");
            }
            else if (num % 2 == 0)
            {
                if (num > 0)
                {
                    printf("EVEN POSITIVE\n");
                }
                else
                {
                    printf("EVEN NEGATIVE\n");
                }
            }
            else
            {
                if (num > 0)
                {
                    printf("ODD POSITIVE\n");
                }
                else
                {
                    printf("ODD NEGATIVE\n");
                }
            }
        }
    }
    return 0;
}