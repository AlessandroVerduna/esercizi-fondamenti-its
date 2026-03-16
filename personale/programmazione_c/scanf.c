#include <stdio.h>

int main(void){
    int a, b, c, d;

    scanf("%d%d%d%d", &a, &b, &c, &d);
    printf("%d|%d|%d|%d\n\n", a, b, c, d);

    int e, f;
    float g, h;

    scanf("%d%d%f%f", &e, &f, &g, &h);
    printf("%d|%d|%f|%f", e, f, g, h);
    return 0;
}