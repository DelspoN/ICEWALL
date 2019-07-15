from pwn import *
import requests

context.log_level="error"

flags = ['FLAG{159b561866d2f691}', 'FLAG{a5acac2ece725c16}', 'FLAG{70d87cbed5b97332}', 'FLAG{cd3e04c43752377d}', 'FLAG{d7ca187fdf3376bf}', 'FLAG{4e4c920dc76433fc}', 'FLAG{99d632eb646b5037}', 'FLAG{03d1907f835d988d}', 'FLAG{9282cad89332c5db}', 'FLAG{2d409fe1b76f2fca}']
hosts = ['163.44.166.49', '133.130.96.251', '150.95.205.77', '118.27.36.108', '118.27.26.81']

# check flags
for ip in hosts:
  s = ssh(user='root',host=ip,port=22,password='Del1324!@')
  p = s.process("/bin/bash")
  p.sendlineafter("# ", "docker exec -it login-test mysql -u sqluser -p")
  p.recvuntil("Enter password: ")
  p.sendline('Passw0rD123')
  p.sendlineafter("mysql> ", "use mydb;")
  p.sendlineafter("mysql> ", "select * from FlaG_i5_heRe;")
  flag = p.recvuntil("FLAG{")[-5:] + p.recvuntil("}")
  print "%s : %s" % (flag, str(flag in flags))
  p.close()
  s.close()

# check flags
for ip in hosts:
  s = ssh(user='root',host=ip,port=22,password='Del1324!@')
  p = s.process("/bin/bash")
  p.sendlineafter("# ", "docker exec php-practice cat /flag; echo 'END'")
  flag = p.recvuntil('END')[:-4]
  p.close()
  s.close()
  print "%s : %s" % (flag, str(flag in flags))

# login-test
ids = ['admin', 'seonguk', 'youngjoong', 'icewall']
pws = ['flag is not here just in db!', 'babobab0', 'cheonjaeman!', 'world-best club']
for ip in hosts:
  s = requests.Session()
  url = "http://%s:20030/login.php" % ip

  for i in range(len(ids)) :
    data = {"id" : ids[i], "pw" : pws[i]}
    res = s.post(url, data=data)
    print "%s : %s : %s" % (ip, str(("Hello, %s" % ids[i]) == res.text), res.text)

for ip in hosts:
  s = requests.Session()
  url = "http://%s:20010/" % ip
  params = {'page' : 'p.php'}

  res = s.get(url, params=params)
  print "%s : %s" % (ip, "This is a p tag" in res.text)

  params = {'page' : 'h1.php'}

  res = s.get(url, params=params)
  print "%s : %s" % (ip, "This is a h1 tag" in res.text)