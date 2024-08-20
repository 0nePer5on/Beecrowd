#include <stdio.h>

int main()
{
    int v[20], j = 0;
    for (int i = 0; i < 20; i++)
    {
        scanf("%d", &v[i]);
    }
    for (int i = 19; i >= 0; i--)
    {
        printf("N[%d] = %d\n", j, v[i]);
        j++;
    }
    return 0;
}