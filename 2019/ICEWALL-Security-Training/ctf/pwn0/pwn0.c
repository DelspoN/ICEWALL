#include <stdio.h>
#include <unistd.h>

int pwn() {
	system("/bin/sh ");
	return 0;
}

int vulnerable() {
	char input[128];
	scanf("%s", input);
	return 0;
}

int main() {
	setbuf(stdin, 0);
	setbuf(stdout, 0);

	puts("PWN0 by DelspoN");
	vulnerable();
	return 0;
}

// gcc -m32 -fno-stack-protector -o pwn0 pwn0.c
