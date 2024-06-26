#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
    int a;
    int b;
    double c;
    char name[80];
} data;

int main (int argc, char *argv[])
{
    FILE * fOut;
    data fred = {0};
    fred.a = 37;
    fred.b = 42;
    fred.c = 3.142;
    strcpy(fred.name,"Hollow World!");

    fOut = fopen ("bindata","w");
    if (!fOut) {
        perror("bindata");
        exit(1);
    }
    fwrite(&fred,sizeof(fred),1,fOut);
    
    fclose(fOut);
    return 0;
}
