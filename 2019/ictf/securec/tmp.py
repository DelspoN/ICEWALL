import subprocess

p = subprocess.Popen('./perfect', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
p.stdin.write('aaa\n')

#print p.stdout.read()
