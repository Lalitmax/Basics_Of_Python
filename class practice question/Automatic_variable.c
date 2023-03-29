#include <stdio.h>

int main()
{
    //  you can also write int a=5; or auto int a=5;
    //    auto int a=5;
    static int a = 5;
    a = 4;

    printf("%d", a);

    return 0;
}