#include <stdio.h>

int main()
{
    int num, conf = 0, cont = 0;
    double media = 0;
    while (conf == 0)
    {
        scanf("%d", &num);
        if (num >= 0)
        {
            media += num;
            cont++;
        }
        else
        {
            conf++;
        }
    }
    printf("%.2lf\n", media / cont);
    return 0;
}