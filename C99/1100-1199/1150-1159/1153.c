#include <stdio.h>

int main()
{
    int n, quant = 1;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        quant *= n - i;
    }
    printf("%d\n", quant);
    return 0;
}