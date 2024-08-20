#include <stdio.h>
#include <string.h>

int main()
{
    int num, res;
    int n[2];
    char val[5][10] = {"pedra", "papel", "tesoura", "lagarto", "Spock"};
    char ent[2][10];
    scanf("%d", &num);
    for (int i = 0; i < num; i++)
    {
        scanf("%s %s", ent[0], ent[1]);
        res = strcmp(ent[0], ent[1]);
        for (int j = 0; j < 2; j++)
        {
            for (int k = 0; k < 5; k++)
            {
                res = strcmp(ent[j], val[k]);
                if (res == 0)
                {
                    n[j] = k;
                }
            }
        }
        if (n[0] == n[1])
        {
            printf("Caso #%d: De novo!\n", i + 1);
        }
        else if ((n[0] == 0 && n[1] == 2) || (n[0] == 0 && n[1] == 3))
        {
            printf("Caso #%d: Bazinga!\n", i + 1);
        }
        else if ((n[0] == 1 && n[1] == 0) || (n[0] == 1 && n[1] == 4))
        {
            printf("Caso #%d: Bazinga!\n", i + 1);
        }
        else if ((n[0] == 2 && n[1] == 1) || (n[0] == 2 && n[1] == 3))
        {
            printf("Caso #%d: Bazinga!\n", i + 1);
        }
        else if ((n[0] == 3 && n[1] == 1) || (n[0] == 3 && n[1] == 4))
        {
            printf("Caso #%d: Bazinga!\n", i + 1);
        }
        else if ((n[0] == 4 && n[1] == 0) || (n[0] == 4 && n[1] == 2))
        {
            printf("Caso #%d: Bazinga!\n", i + 1);
        }
        else
        {
            printf("Caso #%d: Raj trapaceou!\n", i + 1);
        }
    }
    return 0;
}