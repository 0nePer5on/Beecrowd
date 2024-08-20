#include <stdio.h>

int main()
{
    int num;
    double n1, n2, n3;
    scanf("%d", &num);
    for (int i = 0; i < num; i++)
    {
        scanf("%lf %lf %lf", &n1, &n2, &n3);
        n1 = (n1 * 0.2) + (n2 * 0.3) + (n3 * 0.5);
        printf("%.1lf\n", n1);
    }
    return 0;
}