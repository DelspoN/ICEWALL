import random
import sys, os, subprocess
import time

nowPath = '/home/securec' 

def genRandomStr(length):
  ranStr = ''
  for i in xrange(length):
    ranStr += chr(random.randint(65, 91))
  return ranStr

def getCode():
  print "Enter the patched code in base64 format"
  sys.stdout.flush()
  code = raw_input().decode("base64")
  return code

def setPrivateDir():
  with open('/dev/urandom', 'r') as f:
    r = f.read(4)
  path = '%s/tmp/%s' % (nowPath, r.encode('hex'))
  os.system('mkdir %s' % path)
  return path

def compileCode(path, code):
  with open('%s/patched.c' % path, 'w') as f:
    f.write(code)

  target = '%s/patched' % path
  os.system('arm-linux-gnueabi-gcc-5 -o %s %s/patched.c' % (target, path))

  if not os.path.isfile(target):
    print "Compiliation error"
    sys.stdout.flush()
    exit()

  return target

def testCode(target, path):
  for i in range(0x100, 0, -1):
    inp = genRandomStr(i)
    presFile = '%s/presult%d' % (path, i)
    resFile = '%s/result%d' % (path, i)

    cmd = 'echo "%s" | %s/perfect > %s' % (inp, nowPath, presFile)
    os.system(cmd)

    with open(presFile, "r") as f:
      rightRes = f.read()

    cmd = 'echo "%s" | chroot %s ./qemu-arm-static %s > %s' % (inp, nowPath, target.replace(nowPath, ""), resFile)
    os.system(cmd)
    with open(resFile, "r") as f:
      inpRes = f.read()

    if rightRes != inpRes:
      return 1

  return 0

def main():
  try:
    code = getCode()
  except:
    print "[!] failed to read the code"
    sys.stdout.flush()
    exit()

  try:
    path = setPrivateDir()
  except:
    print "[!] failed to set a space for test"
    sys.stdout.flush()
    os.system('rm -rf %s' % path)
    exit()

  try:
    target = compileCode(path, code)
  except Exception as e:
    print "[!] failed to compile the code"
    sys.stdout.flush()
    os.system('rm -rf %s' % path)
    exit()

  try:
    result = testCode(target, path)
  except Exception as e:
    print "[!] failed to test the code"
    sys.stdout.flush()
    os.system('rm -rf %s' % path)
    exit()

  os.system('rm -rf %s' % path)

  if result == 0:
    print "It's safe :)"
    sys.stdout.flush()
    print "ICTF{easy to prevent buffer overflow}"
    sys.stdout.flush()
  else:
    print "It's wrong :("
    sys.stdout.flush()


if __name__ == '__main__':
  main()
