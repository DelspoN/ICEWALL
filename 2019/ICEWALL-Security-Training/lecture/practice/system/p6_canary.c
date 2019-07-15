#include <stdio.h>

int login() {
  char id[32], pw[32], nic[32];
  int auth, yn;

  printf("Here is stack addr : %p\n", &nic);

  while (1) {
    puts("Input your ID : ");
    scanf("%31s", id);
    puts("Input your PW : ");
    scanf("%31s", pw);

    auth = (!strcmp(id, "admin")  && !strcmp(pw, "p@ssw0rd"));

    puts("Input your nicname");
    read(0, nic, 0x100);

    printf("Hello ");
    puts(nic);

    puts("Do you want to break?");
    scanf("%d", &yn);
    getchar();

    if (yn)
      break;
  }

  return auth;
}

int main() {
  int isAuth = 0;

  while (1) {
    if (login() || isAuth) {
      system("echo 'Successful'");
    }
    else {
      system("echo 'Failed'");
    }
  }

  return 0;
}
