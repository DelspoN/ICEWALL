#include <stdio.h>

void func7(int a1, int a2, int a3, int a4, int a5, int a6, int a7) {
  printf("func7 : %d %d %d %d %d %d %d\n", a1, a2, a3, a4, a5, a6, a7);
}

void func6(int a1, int a2, int a3, int a4, int a5, int a6) {
  printf("func6 : %d %d %d %d %d %d\n", a1, a2, a3, a4, a5, a6);
}

void func5(int a1, int a2, int a3, int a4, int a5) {
  printf("func5 : %d %d %d %d %d\n", a1, a2, a3, a4, a5);
}

void func4(int a1, int a2, int a3, int a4) {
  printf("func4 : %d %d %d %d\n", a1, a2, a3, a4);
}

void func3(int a1, int a2, int a3) {
  printf("func3 : %d %d %d\n", a1, a2, a3);
}

void func2(int a1, int a2) {
  printf("func2 : %d %d\n", a1, a2);
  
}

void func1(int a1) {
  printf("func1 : %d\n", a1);
  
}

void func0() {
  printf("func0\n");
}

int main() {
  func0();
  func1(1);
  func2(1,2);
  func3(1,2,3);
  func4(1,2,3,4);
  func5(1,2,3,4,5);
  func6(1,2,3,4,5,6);
  func7(1,2,3,4,5,6,7);
  return 0;
}
