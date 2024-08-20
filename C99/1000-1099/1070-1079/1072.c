#include <stdio.h>

int main()
{
    int n, num, in = 0, out = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &num);
        if (num >= 10 && num <= 20)
        {
            in++;
        }
        else
        {
            out++;
        }
    }
    printf("%d in\n", in);
    printf("%d out\n", out);
    return 0;
}