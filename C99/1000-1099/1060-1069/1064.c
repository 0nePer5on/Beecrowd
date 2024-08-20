#include <stdio.h>

int main()
{
    int cont = 0;
    double n[6], media = 0;
    for (int i = 0; i < 6; i++)
    {
        scanf("%lf", &n[i]);
        if (n[i] > 0)
        {
            cont++;
            media += n[i];
        }
    }
    printf("%d valores positivos\n", cont);
    media /= cont;
    printf("%.1lf\n", media);
    return 0;
}