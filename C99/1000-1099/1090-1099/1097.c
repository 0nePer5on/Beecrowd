#include <stdio.h>

int main()
{
    int j, l = 7;
    for (int k = 1; k <= 9; k += 2)
    {
        j = l;
        for (int i = 0; i < 3; i++)
        {
            printf("I=%d J=%d\n", k, j);
            j--;
        }
        l += 2;
    }
    return 0;
}