#include <stdio.h>
#include <math.h>
int main()
{
    int n;
    scanf("%d", &n);
    printf("VOLUME = %.3lf\n", (4.0 / 3) * 3.14159 * pow(n, 3));
    return 0;
}