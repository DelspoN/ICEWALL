#define _CRT_SECURE_NO_WARNINGS 
#include <stdio.h>

#include<string.h>
int main()
{
    char s1[0x1000];  
    char buffer[0x20];
	

    setvbuf( stdout, NULL, _IONBF, 0 );
	scanf("%s",s1);
	strcpy(buffer,"ICTF{format_stirng_bug_to_leak}");
    printf(s1);
    return 0;
}
