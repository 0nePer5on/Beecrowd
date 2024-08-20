#include <stdio.h>

int main()
{
    int n, conf = 0, conf2 = 0, cont;
    while (conf == 0)
    {
        scanf("%d", &n);
        cont = 0;
        conf2 = 0;
        if (n != 0)
        {
            while (conf2 < 5)
            {
                if (n % 2 == 0)
                {
                    cont += n;
                    conf2++;
                }
                n++;
            }
            printf("%d\n", cont);
        }
        else
        {
            conf++;
        }
    }
    return 0;
}