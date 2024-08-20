#include <stdio.h>
#include <math.h>

int main()
{
    int diaI, horaI, minI, segI, diaF, horaF, minF, segF;
    scanf("Dia %d", &diaI);
    scanf("%d : %d : %d\n", &horaI, &minI, &segI);
    scanf("Dia %d", &diaF);
    scanf("%d : %d : %d", &horaF, &minF, &segF);
    diaI = diaF - diaI;
    horaI = horaF - horaI;
    minI = minF - minI;
    segI = segF - segI;
    if (segI < 0)
    {
        segI += 60;
        minI--;
    }
    if (minI < 0)
    {
        minI += 60;
        horaI--;
    }
    if (horaI < 0)
    {
        horaI += 24;
        diaI--;
    }

    printf("%d dia(s)\n", diaI);
    printf("%d hora(s)\n", horaI);
    printf("%d minuto(s)\n", minI);
    printf("%d segundo(s)\n", segI);
    return 0;
}