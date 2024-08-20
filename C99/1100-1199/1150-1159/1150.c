#include <stdio.h>

int main()
{
    int n1, n2, conf = 0, cont = 0, i = 0;
    scanf("%d", &n1);
    while (conf == 0)
    {
        scanf("%d", &n2);
        if (n1 < n2)
        {
            conf++;
        }
    }
    while (cont < n2)
    {
        cont += n1 + i;
        i++;
    }
    printf("%d\n", i);
    return 0;
}