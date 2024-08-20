#include <stdio.h>

int main()
{
    int num, n1, n2;
    scanf("%d", &num);
    for (int i = 0; i < num; i++)
    {
        scanf("%d %d", &n1, &n2);
        printf("%d\n", n1 + n2);
    }
    return 0;
}