#include <stdio.h>

int main()
{
    int i, n1 = 0, n2 = 1, conf = 0, quant, num = 0;
    while (conf == 0)
    {
        scanf("%d", &quant);
        printf("0 ");
        for (i = 0; i < quant - 1; i++)
        {
            if (i < quant - 2)
            {
                printf("%d ", n2);
                num = n1 + n2;
                n1 = n2;
                n2 = num;
            }
            else
            {
                printf("%d\n", n2);
            }
        }
        conf++;
    }
    return 0;
}