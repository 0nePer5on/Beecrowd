#include <stdio.h>
#include <math.h>

int main()
{
    int n1, n2, n3, maiorAB, maiorABC;
    scanf("%d %d %d", &n1, &n2, &n3);
    maiorAB = (n1 + n2 + abs(n1 - n2)) / 2;
    maiorABC = (maiorAB + n3 + abs(maiorAB - n3)) / 2;
    printf("%d eh o maior\n", maiorABC);
    return 0;
}