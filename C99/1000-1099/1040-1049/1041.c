#include <stdio.h>

int main()
{
    double n1, n2;
    scanf("%lf %lf", &n1, &n2);
    if (n1 == 0 && n2 == 0)
    {
        printf("Origem\n");
    }
    else if (n1 > 0 && n2 > 0)
    {
        printf("Q1\n");
    }
    else if (n1 < 0 && n2 > 0)
    {
        printf("Q2\n");
    }
    else if (n1 > 0 && n2 < 0)
    {
        printf("Q4\n");
    }
    else if (n1 < 0 && n2 < 0)
    {
        printf("Q3\n");
    }
    else if (n2 == 0)
    {
        printf("Eixo X\n");
    }
    else if (n1 == 0)
    {
        printf("Eixo Y\n");
    }
    return 0;
}