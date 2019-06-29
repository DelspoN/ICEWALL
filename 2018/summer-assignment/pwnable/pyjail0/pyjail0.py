# -*- encoding:utf-8 -*-
import os,sys

print "DELSPON's PYTHON JAIL"
sys.stdout.flush()

while True:
	print ">> ",
	sys.stdout.flush()
	code = raw_input()
	if "exit" in code:
		break
	os.system("python -c \"" + code + "\"")
exit()
