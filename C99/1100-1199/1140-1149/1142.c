#include <stdio.h>

int main()
{
    int num, cont = 0, conf = 0, j = 1;
    scanf("%d", &num);
    for (int i = 0; i < num; i++)
    {
        while (conf == 0)
        {
            cont++;
            if (cont == 4)
            {
                printf("PUM\n");
                cont = 0;
                if (num * 4 == j)
                {
                    conf++;
                }
            }
            else
            {
                printf("%d ", j);
            }
            j++;
        }
    }
    return 0;
}