#include <stdio.h>

int main()
{
    int k = 11;
    double soma = 0, m[12][12], cont = 0.0;
    char c;
    scanf("%c", &c);
    for (int i = 0; i < 12; i++)
    {
        for (int j = 0; j < 12; j++)
        {
            scanf("%lf", &m[i][j]);
        }
    }
    for (int i = 0; i < 12; i++)
    {
        for (int j = 0; j < 12; j++)
        {
            if (i < j && i > 12 - j - 1)
            {
                soma += m[i][j];
                cont++;
            }
        }
    }
    if (c == 'M')
    {
        soma /= cont;
    }
    printf("%.1lf\n", soma);
    return 0;
}