# -*- encoding:utf-8 -*-
import os,sys

print "DELSPON's PYTHON JAIL"
sys.stdout.flush()

banned = ["\"", ";", " ", "'", "cat", "flag", "*", "read", "open"]
print "You can't use " + str(banned)

while True:
	print ">> ",
	sys.stdout.flush()
	code = raw_input()

	ban_flag = 0
	for i in banned:
		if i in code:
			print "BANNED : " + i
			sys.stdout.flush()
			ban_flag = 1

	if ban_flag:
		continue

	if "exit" in code:
		break

	os.system("python -c \"" + code + "\"")
exit()
