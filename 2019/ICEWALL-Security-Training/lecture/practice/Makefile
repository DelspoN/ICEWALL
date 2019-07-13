all:
	gcc -o p0 p0.c
	gcc -o p1 p1.c
	gcc -o p2 p2.c
	gcc -o p3 p3.c
	gcc -o p4 p4.c
	gcc -o p5_32 p5.c -m32
	gcc -o p5_64 p5.c
	gcc -o p6_32_0 p6.c -m32 -z execstack -fno-stack-protector
	gcc -o p6_32_1 p6.c -m32 -fno-stack-protector
	gcc -o p6_32_2 p6.c -m32
	gcc -o p6_64_0 p6.c -z execstack -fno-stack-protector
	gcc -o p6_64_1 p6.c -fno-stack-protector
	gcc -o p6_64_2 p6.c
