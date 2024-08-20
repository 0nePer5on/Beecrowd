#include <stdio.h>

int main()
{
    int k = 5, l = 7;
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
    for (int i = 7; i < 12; i++)
    {
        for (int j = k; j < l; j++)
        {
            soma += m[i][j];
        }
        k--;
        l++;
    }
    if (c == 'M')
    {
        soma /= 30.0;
    }
    printf("%.1lf\n", soma);
    return 0;
}