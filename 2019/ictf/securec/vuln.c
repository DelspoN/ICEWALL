#include <stdio.h>

int main() {
  char buf[0x40];
  gets(buf);
  puts(buf);
  return 0;
}
