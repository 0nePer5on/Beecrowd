#include <stdio.h>
#include <math.h>

int main()
{
    double n1, pi = 3.14159;
    scanf("%lf", &n1);
    printf("A=%.4lf\n", pi * (pow(n1, 2)));
    return 0;
}