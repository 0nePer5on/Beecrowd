#include <stdio.h>

int main()
{
    int n, cont = 0;
    scanf("%d", &n);
    for (int i = 0; i < 1000; i++)
    {
        if (cont < n)
        {
            printf("N[%d] = %d\n", i, cont);
            cont++;
        }
        else
        {
            cont = 0;
            i--;
        }
    }
    return 0;
}