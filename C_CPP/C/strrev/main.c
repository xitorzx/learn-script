#include <stdio.h>
#include <string.h>
#include "strrev.h"
int main()
{
    char str[20]= "hello world!";
    printf("%s",strrev(str));
    getchar();
    return 0;
}
