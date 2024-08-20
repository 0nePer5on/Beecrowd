#include <stdio.h>

int main()
{
    int n1, n2, aux, cont = 0;
    scanf("%d %d", &n1, &n2);
    if (n1 < n2)
    {
        aux = n1;
        n1 = n2;
        n2 = aux;
    }
    for (int i = n2; i < n1; i++)
    {
        if (i % 13 != 0)
        {
            cont += i;
        }
    }
    printf("%d\n", cont);
    return 0;
}