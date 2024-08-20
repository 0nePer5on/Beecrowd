#include <stdio.h>

int main()
{
    int num, n1, n2, conf, cont = 0;
    scanf("%d", &num);
    for (int i = 0; i < num; i++)
    {
        scanf("%d %d", &n1, &n2);
        conf = 0;
        cont = 0;
        while (conf < n2)
        {
            if (n1 % 2 != 0)
            {
                cont += n1;
                conf++;
            }
            n1++;
        }
        printf("%d\n", cont);
    }
    return 0;
}