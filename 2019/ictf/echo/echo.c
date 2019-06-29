#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main() {
  char msg[0x40];
  char cmd[0x80];

  setbuf(stdin, 0);
  setbuf(stdout, 0);

  printf("enter your message : ");
  scanf("%63s", msg);

  sprintf(cmd,"echo \"%s\"", msg);

  system(cmd);
  return 0;
}
