#include <stdio.h>

int main()
{
    int n1, n2;
    double n3, total = 0;
    scanf("%d %d %lf", &n1, &n2, &n3);
    total += n2 * n3;
    scanf("%d %d %lf", &n1, &n2, &n3);
    total += n2 * n3;
    printf("VALOR A PAGAR: R$ %.2lf\n", total);
    return 0;
}