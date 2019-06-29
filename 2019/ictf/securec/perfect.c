#include <stdio.h>

int main() {
  char buf[0x40];
  scanf("%63s", buf);
  puts(buf);
  return 0;
}
