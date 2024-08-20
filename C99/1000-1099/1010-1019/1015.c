#include <stdio.h>
#include <math.h>

int main()
{
    double n1, n2, n3, n4;
    scanf("%lf %lf %lf %lf", &n1, &n2, &n3, &n4);
    printf("%.4lf\n", sqrt(pow((n3 - n1), 2) + pow((n4 - n2), 2)));
    return 0;
}