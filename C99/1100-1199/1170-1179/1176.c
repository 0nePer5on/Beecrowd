#include <stdio.h>

int main()
{
    int num, num2;
    long long int f[100], n1 = 0, n2 = 1, aux;
    f[0] = n1;
    for (int i = 1; i < 100; i++)
    {
        f[i] = n2;
        aux = n2;
        n2 += n1;
        n1 = aux;
    }
    scanf("%d", &num);
    for (int i = 0; i < num; i++)
    {
        scanf("%d", &num2);
        printf("Fib(%d) = %lld\n", num2, f[num2]);
    }
    return 0;
}