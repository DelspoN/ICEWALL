#include <stdio.h>
#include <stdlib.h>

int main() {
  char input[32], command[64];
  scanf("%31s", input);
  sprintf(command, "echo \"%s\"", input);
  system(command);
  return 0;
}
