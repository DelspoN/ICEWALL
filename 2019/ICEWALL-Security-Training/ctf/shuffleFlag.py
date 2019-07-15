with open("/dev/urandom", "r") as f:
	flag = f.read(8).encode("hex")
	flag = "FLAG{%s}" % flag

with open("./login-test/set.sql", "r") as f:
	content = f.read()

with open("./login-test/set.sql", "w") as f:
	content = content.replace("FLAG{thisistestflag}", flag)
	f.write(content)

with open("/dev/urandom", "r") as f:
	flag = f.read(8).encode("hex")
	flag = "FLAG{%s}" % flag

with open("./php-practice/flag", "r") as f:
	content = f.read()

with open("./php-practice/flag", "w") as f:
	content = content.replace("FLAG{thisistestflag}", flag)
	f.write(content)