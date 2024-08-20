#include <stdio.h>

int main()
{
    int l;
    double soma = 0, m[12][12];
    char c;
    scanf("%d %c", &l, &c);
    for (int i = 0; i < 12; i++)
    {
        for (int j = 0; j < 12; j++)
        {
            scanf("%lf", &m[i][j]);
        }
    }
    for (int i = 0; i < 12; i++)
    {
        soma += m[l][i];
    }
    if (c == 'M')
    {
        soma /= 12.0;
    }
    printf("%.1lf\n", soma);
    return 0;
}