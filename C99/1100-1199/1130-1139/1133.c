#include <stdio.h>

int main()
{
    int n1, n2, aux;
    scanf("%d %d", &n1, &n2);
    if (n1 < n2)
    {
        aux = n1;
        n1 = n2;
        n2 = aux;
    }
    for (int i = n2 + 1; i < n1; i++)
    {
        if (i % 5 == 2 || i % 5 == 3)
        {
            printf("%d\n", i);
        }
    }
    return 0;
}