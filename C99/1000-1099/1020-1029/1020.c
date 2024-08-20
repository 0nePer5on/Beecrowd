#include <stdio.h>

int main()
{
    int n, ano = 0, mes = 0;
    scanf("%d", &n);
    if (n >= 365)
    {
        ano = n / 365;
        n %= 365;
    }
    if (n >= 30)
    {
        mes = n / 30;
        n %= 30;
    }
    printf("%d ano(s)\n", ano);
    printf("%d mes(es)\n", mes);
    printf("%d dia(s)\n", n);
    return 0;
}