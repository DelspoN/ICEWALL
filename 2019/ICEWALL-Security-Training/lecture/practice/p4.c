#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void filter(char * input) {
  char * filter_char = "$`;|&";
  for (int i = 0; i < strlen(filter_char); i++) {
    for (int j = 0; j < strlen(input); j++) {
      if(input[j] == filter_char[i]) {
        puts(input);
        puts("no");
        exit(0);
      }
    }
  }

  char * p = strchr(input, '\"');
  while (p) {
    for (int i = strlen(p); i > 0; i--)
      p[i] = p[i-1];
    p[0] = '\\';
    p[1] = '\"';
    p = strchr(p+2, '\"');
  }

}

int main() {
  setbuf(stdin, 0);
  char input[32], command[64];
  read(0, input, 31);
  input[31] = 0;

  filter(&input);
  sprintf(command, "echo \"%s\"", input);
  system(command);
  return 0;
}
