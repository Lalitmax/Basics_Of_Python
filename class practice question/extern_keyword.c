#include <stdio.h>
#include<temp.c>
int showglobal();
int sum = 67;   // this global variable


void main()
{
    // int s = showglobal();
    // printf("%d", s);

    int s=hello(5);
    printf("%d",s);
}

int showglobal()


{
    // extern keyword is used to kisi bhi global value ko apne me chipkana
    extern int sum;
    return sum;
}
