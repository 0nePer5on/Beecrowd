#include <stdio.h>

int main()
{
    int num, n, p, menor;
    scanf("%d", &num);
    scanf("%d", &menor);
    p = 0;
    for (int i = 1; i < num; i++)
    {
        scanf("%d", &n);
        if (menor > n)
        {
            menor = n;
            p = i;
        }
    }
    printf("Menor valor: %d\n", menor);
    printf("Posicao: %d\n", p);
    return 0;
}