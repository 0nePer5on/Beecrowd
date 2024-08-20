#include <stdio.h>
#include <string.h>

int main()
{
    char nome[100];
    double n1, n2;
    scanf("%s %lf %lf", nome, &n1, &n2);
    n2 *= 0.15;
    printf("TOTAL = R$ %.2lf\n", n1 + n2);
    return 0;
}