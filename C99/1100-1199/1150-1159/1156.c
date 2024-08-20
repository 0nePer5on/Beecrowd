#include <stdio.h>

int main()
{
    int conf = 0;
    double s = 1.0, i = 3.0, j = 2.0;
    while (conf == 0)
    {
        if (i != 39)
        {
            s += i / j;
            i += 2;
            j *= 2;
        }
        else
        {
            conf++;
        }
    }
    printf("%.2lf\n", s);
    return 0;
}