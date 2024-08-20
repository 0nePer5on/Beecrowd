#include <stdio.h>
#include <math.h>

int main()
{
    int n1, n2, n3, n4, total, h, m;
    scanf("%d %d %d %d", &n1, &n2, &n3, &n4);
    total = (n3 * 60 + n4) - (n1 * 60 + n2);
    if (total < 1)
    {
        total += 24 * 60;
    }
    h = total / 60;
    m = total % 60;
    printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)\n", h, m);
    return 0;
}