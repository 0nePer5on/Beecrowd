#include <stdio.h>

int main()
{
    int n, conf = 0;
    while (conf == 0)
    {
        scanf("%d", &n);
        if (n != 0)
        {
            for (int i = 1; i <= n; i++)
            {
                if (i < n)
                {
                    printf("%d ", i);
                }
                else
                {
                    printf("%d\n", i);
                }
            }
        }
        else
        {
            conf++;
        }
    }
    return 0;
}