# -*- encoding:utf-8 -*-
from flask import Flask, render_template, render_template_string, request
import sqlite3
import urllib2
from selenium import webdriver

app = Flask(__name__)

createtable = """CREATE TABLE IF NOT EXISTS contact (
id integer PRIMARY KEY AUTOINCREMENT,
email text,
message text,
is_checked integer DEFAULT 0
);
"""

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/contact")
def login():
	return render_template('contact.html')

@app.route("/submit", methods=['GET'])
def submit():
	email = request.args.get('email')
	message = request.args.get('message')

	conn = sqlite3.connect("/tmp/mydb.db")
	cur = conn.cursor()
	cur.execute(createtable)

	sql = "insert into contact(email, message) values (?, ?);"
	cur.execute(sql, (email, message))
	conn.commit()
	conn.close()

	bot()

	return "<script>alert(\"접수 완료\"); history.back(-1);</script>"

@app.route("/admin", methods=['GET'])
def admin():
	_id = request.args.get('_id')
	_pw = request.args.get('_pw')
	_email = request.args.get('email')

	if not (_id == "admin" and _pw == "ICTF{it is a baby xss}"):
		return "do not hack!"

	conn = sqlite3.connect("/tmp/mydb.db")
	cur = conn.cursor()
	cur.execute(createtable)

	sql = "select * from contact where is_checked = 0 limit 1;"

	if _email is not None:
		sql = "select * from contact where email = '%s' limit 1;" % _email.replace("'", "''")

	cur.execute(sql)
	rows = cur.fetchall()

	if len(rows) == 0:
		conn.close()
		return "None"

	idx = rows[0][0]
	email = rows[0][1]
	message = rows[0][2]
	is_checked = rows[0][3]

	sql = "update contact set is_checked = 1 where id = %d" % idx
	cur.execute(sql)
	conn.commit()
	conn.close()

	result = """
	idx : %d<br>
	email : %s<br>
	message : %s<br>
	is_checked : %d<br>
	""" % (idx, email, message, is_checked)

	return result

@app.route("/archiver", methods=['GET'])
def archiver():
	url = request.args.get('url')
	r = urllib2.Request(url)
	r.add_header('Referer', request.url)
	return urllib2.urlopen(r).read()

def bot():
	options = webdriver.ChromeOptions()
	options.add_argument('headless')
	options.add_argument('window-size=1920x1080')
	options.add_argument("disable-gpu")
	options.add_argument("--no-sandbox")
	driver = webdriver.Chrome('./chromedriver', chrome_options=options)
	driver.get('http://localhost/archiver?url=http%3A%2F%2Flocalhost%2Fadmin%3F_id%3Dadmin%26_pw%3DICTF%7Bit%20is%20a%20baby%20xss%7D')
	driver.implicitly_wait(1)
	driver.quit()

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True, port=80)
