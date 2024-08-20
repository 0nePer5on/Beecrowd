#include <stdio.h>

int main()
{
    int n, h = 0, m, s;
    scanf("%d", &n);
    m = n / 60;
    s = n % 60;
    if (m >= 60)
    {
        h = m / 60;
        m %= 60;
    }
    printf("%d:%d:%d\n", h, m, s);
    return 0;
}