#include <stdio.h>

int main()
{
    double n;
    int conf = 0;
    scanf("%lf", &n);
    if (n >= 0 && n <= 2000)
    {
        conf++;
    }
    else if (n > 2000 && n <= 3000)
    {
        n = (n - 2000) * 0.08;
    }
    else if (n > 3000 && n <= 4500)
    {
        n = (1000 * 0.08) + ((n - 3000) * 0.18);
    }
    else if (n > 4500)
    {
        n = (1000 * 0.08) + (1500 * 0.18) + ((n - 4500) * 0.28);
    }
    if (conf == 1)
    {
        printf("Isento\n");
    }
    else
    {
        printf("R$ %.2lf\n", n);
    }
    return 0;
}