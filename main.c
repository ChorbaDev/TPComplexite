#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, const char * argv[]) {
    int m, p;

    srand((unsigned int)time(NULL));

    printf("Entrez le nombre de marqueurs positifs : ");
    scanf("%d", &p);
    printf("Entrez le nombre de marqueurs : ");
    scanf("%d", &m);

    test(p, m);

    return 0;
}