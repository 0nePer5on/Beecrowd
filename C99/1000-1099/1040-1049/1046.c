#include <stdio.h>
#include <math.h>

int main()
{
    int n1, n2;
    scanf("%d %d", &n1, &n2);

    if (n1 > n2)
    {
        n2 += 24;
        n1 = abs(n1 - n2);
        printf("O JOGO DUROU %d HORA(S)\n", n1);
    }
    else if (n1 == n2)
    {
        printf("O JOGO DUROU 24 HORA(S)\n");
    }
    else
    {
        n2 = abs(n2 - n1);
        printf("O JOGO DUROU %d HORA(S)\n", n2);
    }
    return 0;
}