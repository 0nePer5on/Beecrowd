#include <stdio.h>

int main()
{
    int v[10], n;
    for (int i = 0; i < 10; i++)
    {
        scanf("%d", &n);
        if (n > 0)
        {
            v[i] = n;
        }
        else
        {
            v[i] = 1;
        }
        printf("X[%d] = %d\n", i, v[i]);
    }
    return 0;
}