#include<stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

void main(){
        setvbuf( stdout, NULL, _IONBF, 0 );
	int fd;
        fd = open("/home/format/flag", O_RDONLY);
	char buffer[0x20];
	char input[0x400];

	scanf("%s",input);
	read(fd,buffer,31);

	printf(input);
}



