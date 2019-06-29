#include<stdlib.h>
#include<stdio.h>
#include <stdlib.h>


int print(int size, char* buffer){
	int result;
	write(1,buffer,size);
	return 0;
}

int edit(int size, char* buffer){
	int result;
	result=read(0, buffer,size);
	if (result==-1){
		printf("Oh. failed to edit memo. Try again.\n");
		return 0;
	}
	else{
		printf("Ok. success to edit memo.\n");
		return 1;
	}
}

void main(){
	char buffer[0x40];
	int select;
	int size;
        setvbuf( stdout, NULL, _IONBF, 0 );

	while (1){

		printf("1: edit memo\n2: print memo\n3: exit\n");
		scanf("%d",&select);
		if (select==1){
			printf("size: ");
			scanf("%d",&size);
			if (!edit(size,buffer)){
				break;
			}
		}
		else if(select==2){
			printf("size: ");
			scanf("%d",&size);
			print(size,buffer);
		}
		else if(select==3){
			break;

		}
		else{break;}
}
}
