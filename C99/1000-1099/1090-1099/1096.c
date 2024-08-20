#include <stdio.h>

int main()
{
    int j;
    for (int k = 1; k <= 9; k += 2)
    {
        j = 7;
        for (int i = 0; i < 3; i++)
        {
            printf("I=%d J=%d\n", k, j);
            j--;
        }
    }
    return 0;
}