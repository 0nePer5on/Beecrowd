#include <stdio.h>

int main()
{
    double n1, n2, n3, n4, media, ex;
    scanf("%lf %lf %lf %lf", &n1, &n2, &n3, &n4);
    n1 *= 0.2;
    n2 *= 0.3;
    n3 *= 0.4;
    n4 *= 0.1;
    media = n1 + n2 + n3 + n4;
    printf("Media: %.1lf\n", media);
    if (media >= 7)
    {
        printf("Aluno aprovado.\n");
    }
    else if (media >= 5 && media < 7)
    {
        printf("Aluno em exame.\n");
        scanf("%lf", &ex);
        media = (media + ex) / 2;
        printf("Nota do exame: %.1lf\n", ex);
        if (media >= 5)
        {
            printf("Aluno aprovado.\n");
        }
        else
        {
            printf("Aluno reprovado.\n");
        }
        printf("Media final: %.1lf\n", media);
    }
    else if (media < 5)
    {
        printf("Aluno reprovado.\n");
    }
    return 0;
}