#include <stdio.h>
#include <stdlib.h>

int main()
{
    int p, j1, j2, r, a;
    int par;
    scanf("%d %d %d %d %d", &p, &j1, &j2, &r, &a);
    if (r == 1)
    {
        if (a == 1)
        {
            printf("Jogador 2 ganha!\n");
        }
        else
        {
            printf("Jogador 1 ganha!\n");
        }
    }
    else
    {
        if (a == 1)
        {
            printf("Jogador 1 ganha!\n");
        }
        else
        {
            if ((j1 + j2) % 2 == 0)
            {
                par = 1;
            }
            else
            {
                par = 0;
            }
            if (p == 1)
            {
                if (par == 1)
                {
                    printf("Jogador 1 ganha!\n");
                }
                else
                {
                    printf("Jogador 2 ganha!\n");
                }
            }
            else
            {
                if (par == 1)
                {
                    printf("Jogador 2 ganha!\n");
                }
                else
                {
                    printf("Jogador 1 ganha!\n");
                }
            }
        }
    }
    return 0;
}