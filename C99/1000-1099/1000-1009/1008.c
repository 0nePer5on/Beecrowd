#include <stdio.h>

int main()
{
    int n1, n2;
    double n3;
    scanf("%d %d %lf", &n1, &n2, &n3);
    printf("NUMBER = %d\n", n1);
    printf("SALARY = U$ %.2lf\n", n2 * n3);
    return 0;
}