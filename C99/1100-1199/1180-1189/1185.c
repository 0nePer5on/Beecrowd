#include <stdio.h>

int main()
{
    int k = 11;
    double soma = 0, m[12][12];
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
        for (int j = 0; j < k; j++)
        {
            soma += m[i][j];
        }
        k--;
    }
    if (c == 'M')
    {
        soma /= 66.0;
    }
    printf("%.1lf\n", soma);
    return 0;
}