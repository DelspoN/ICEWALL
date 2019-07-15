#include <stdio.h>
#include <unistd.h>

int vulnerable() {
	char input[128], yn = 'y';
	while(yn == 'y') {
		int i = 0;
		while(1) {
			read(0, input + i, 1);
			if (input[i++] == '\n')
				break;
		}
		printf("your input : %s\n", input);
		printf("continue? (y/n) : ");
		scanf("%c", &yn);
	}
	return 0;
}

int main() {
	setbuf(stdin, 0);
	setbuf(stdout, 0);

	puts("PWN2 by DelspoN");
	vulnerable();
	return 0;
}

// gcc -o pwn2 pwn2.c
