import git
import os, sys

message = """#################################################################
ASSIGNMENT #0
00. You have to make program for the following specifications.
01. When the string entered, it must be print.
02. You have to write the Makefile.
03. As a result of 'make', the file named 'main' must be generated.
#################################################################"""

print(message)
sys.stdout.flush()

url = raw_input('enter your git repository : ')

with open('/dev/urandom', 'r') as f:
  randomStr = f.read(8).encode('hex')

path = '/tmp/%s' % randomStr
os.system('mkdir %s' % path)

print("[+] cloning %s" % url)

if url[-4:] != '.git':
  url += '.git'

try:
  git.Git(path).clone(url)
except:
  print("[!] wrong")
  os.system('rm -rf %s' % path)
  exit()

dirName = url[url.rfind("/")+1:-4]
os.chdir(path+'/%s' % dirName)

if not os.path.isfile('./Makefile'):
  print("[!] Makefile not exist")
  os.system('rm -rf %s' % path)
  exit()

print("[+] compiling")
os.system('make')

if not os.path.isfile('./main'):
  print("[!] wrong Makefile")
  os.system('rm -rf %s' % path)
  exit()

testInput = 'ICEWALL is the world best club'
os.system("echo '%s' | ./main > ./result" % testInput)
with open('./result', 'r') as f:
  res = f.read()
print res
if res == testInput:
  print("[+] perfect! your score is 100")
else:
  print("[!] wrong implementation")

os.system('rm -rf %s' % path)

