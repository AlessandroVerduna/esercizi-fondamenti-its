#include <stdio.h>

int main(void)
{
    int base, altezza;
    printf("Inserisci un numero intero per la base: ");
    scanf("%d", &base);
    printf("Inserisci un intero per l'altezza: ");
    scanf("%d", &altezza);
    printf("\nL'area è: %d", base * altezza);
    return 0;
}
