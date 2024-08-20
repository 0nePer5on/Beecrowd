#include <stdio.h>

int main()
{
    int v[10], n;
    scanf("%d", &n);
    for (int i = 0; i < 10; i++)
    {
        v[i] = n;
        n *= 2;
        printf("N[%d] = %d\n", i, v[i]);
    }
    return 0;
}