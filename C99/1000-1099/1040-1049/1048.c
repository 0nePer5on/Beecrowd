#include <stdio.h>

int main()
{
    double n, r;
    int p;
    scanf("%lf", &n);
    if (n >= 0 && n <= 400)
    {
        r = n * 0.15;
        n += r;
        p = 15;
    }
    else if (n > 400 && n <= 800)
    {
        r = n * 0.12;
        n += r;
        p = 12;
    }
    else if (n > 800 && n <= 1200)
    {
        r = n * 0.10;
        n += r;
        p = 10;
    }
    else if (n > 1200 && n <= 2000)
    {
        r = n * 0.07;
        n += r;
        p = 7;
    }
    else if (n > 2000)
    {
        r = n * 0.04;
        n += r;
        p = 4;
    }
    printf("Novo salario: %.2f\n", n);
    printf("Reajuste ganho: %.2f\n", r);
    printf("Em percentual: %d %\n", p);
    return 0;
}