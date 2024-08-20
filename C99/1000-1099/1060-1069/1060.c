#include <stdio.h>

int main()
{
    int cont = 0;
    double n[6];
    for (int i = 0; i < 6; i++)
    {
        scanf("%lf", &n[i]);
        if (n[i] > 0)
        {
            cont++;
        }
    }
    printf("%d valores positivos\n", cont);
    return 0;
}