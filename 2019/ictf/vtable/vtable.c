#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct memo {
 void (*show)(char *);
 char * content;
} memo;

int main() {
  setbuf(stdin, 0);
  setbuf(stdout, 0);

  system("echo 'Welcome to memo system'");

  memo * input[10];
  for(int i = 0; i < 10; i++) {
    input[i] = (memo *)malloc(sizeof(memo));
    input[i]->show = puts;
    input[i]->content = (char *)malloc(0x48);
  }
  for(int i = 0; i < 10; i++) {
    printf("Enter your memo[%d]\n", i);
    scanf("%s", input[i]->content);
    input[i]->show(input[i]->content);
  }
  
  return 0;
}
