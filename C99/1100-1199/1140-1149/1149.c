#include <stdio.h>

int main()
{
    int n1, n2, conf = 0, cont = 0;
    scanf("%d", &n1);
    while (conf == 0)
    {
        scanf("%d", &n2);
        if (n2 > 0)
        {
            conf++;
        }
    }
    for (int i = 0; i < n2; i++)
    {
        cont += n1 + i;
    }
    printf("%d\n", cont);
    return 0;
}