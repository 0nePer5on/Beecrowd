#include <stdio.h>

int main()
{
    int n1, n2, j = 1;
    scanf("%d %d", &n1, &n2);
    while (j != n2 + 1)
    {
        for (int i = 0; i < n1; i++)
        {
            if (i < n1 - 1)
            {
                printf("%d ", j);
            }
            else
            {
                printf("%d\n", j);
            }
            j++;
        }
    }
    return 0;
}