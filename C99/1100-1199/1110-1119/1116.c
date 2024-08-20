#include <stdio.h>

int main()
{
    int num, n1, n2;
    double res;
    scanf("%d", &num);
    for (int i = 0; i < num; i++)
    {
        scanf("%d %d", &n1, &n2);
        if (n2 != 0)
        {
            res = (double)n1 / n2;
            printf("%.1lf\n", res);
        }
        else
        {
            printf("divisao impossivel\n");
        }
    }
    return 0;
}