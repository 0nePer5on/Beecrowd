#include <stdio.h>

int main()
{
    double n1, n2, n3;
    scanf("%lf %lf %lf", &n1, &n2, &n3);
    n1 *= 0.2;
    n2 *= 0.3;
    n3 *= 0.5;
    printf("MEDIA = %.1lf\n", n1 + n2 + n3);
    return 0;
}