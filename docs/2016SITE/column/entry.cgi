#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
import cgitb
# cgitb.enable()
import os
# import Cookie
# import sqlite3
# import commands
import datetime
import random
import hashlib
import base64
import urllib2
import time
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

USERNAME = "tdupress"
PASSWORD = "tdupress"

login_page = '''Content-Type: text/html

<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<title>ログイン画面</title>
</head>

<body>
	<CENTER>
	<h1>ログインしてください</h1>
	<form action="login.cgi" method="post">
		<p>ユーザ名<input type="text" name="username" /></p>
		<p>パスワード<input type="password" name="password" /></p>
		<input type="submit" value="ログイン"/>
	</form>
	%s
	</CENTER>
</body>

</html>
'''

yuruyuri="""Content-Type: text/html

<html lang="ja">
<head>
	<meta charset="UTF-8" />
<head>

<body>
%s
</body>

</html>
"""

page="""Content-Type: text/html

<html lang="ja">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <title>TDUPRESSのコラム達</title>
    <link href="../css2/bootstrap.min.css" rel="stylesheet">
    <link href="../css2/clean-blog.min.css" rel="stylesheet">
    <link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href='http://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
    <link href='http://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>
</head>
<body>
    <nav class="navbar navbar-default navbar-custom navbar-fixed-top">
        <div class="container-fluid">
            <div class="navbar-header page-scroll">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="../index.html">TOP</a>
            </div>
        </div>
    </nav>
    <header class="intro-header" style="background-image: url('../img/home-bg.jpg')">
        <div class="container">
            <div class="row">
                <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
                    <div class="site-heading">
                        <h1>TDUPRESS</h1>
                        <hr class="small">
                        <span class="subheading">新聞委員会メンバーのコラム、集めてみました</span>
                    </div>
                </div>
            </div>
        </div>
    </header>
    <div class="container">
        <div class="row">
            <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
            %s
            </div>
        </div>
    </div>
    <hr>
    <footer>
        <div class="container">
            <div class="row">
                <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
                    <ul class="list-inline text-center">
                        <li>
                            <a href="https://twitter.com/tdupress5507d">
                                <span class="fa-stack fa-lg">
                                    <i class="fa fa-circle fa-stack-2x"></i>
                                    <i class="fa fa-twitter fa-stack-1x fa-inverse"></i>
                                </span>
                            </a>
                        </li>
                        <li>
                            <a href="https://github.com/tdupress">
                                <span class="fa-stack fa-lg">
                                    <i class="fa fa-circle fa-stack-2x"></i>
                                    <i class="fa fa-github fa-stack-1x fa-inverse"></i>
                                </span>
                            </a>
                        </li>
                    </ul>
                    <p class="copyright text-muted">Copyright &copy; TDURESS2016</p>
                </div>
            </div>
        </div>
    </footer>
    <script src="../js/jquery.js"></script>
    <script src="../js/bootstrap.min.js"></script>
    <script src="../js/clean-blog.min.js"></script>
</body>
</html>
"""

post="""
<div class="post-preview">
    <a href="%s">
        <h2 class="post-title">
            %s
        </h2>
        <h3 class="post-subtitle">
            %s
        </h3>
    </a>
</div>
<hr>
"""

hatena_url = "https://blog.hatena.ne.jp/dendai_tarou/dendai-tarou.hatenablog.com/atom/entry"
hatena_id = "dendai_tarou"
hatena_password = "a49isui6er"

def create_wsse(username, password):
    nonce = hashlib.sha1(str(time.time()) + str(random.random())).digest()
    created = datetime.datetime.now().isoformat() + "Z"
    digest = base64.b64encode(hashlib.sha1(nonce+created+password).digest())
    return 'UsernameToken Username="{0}", PasswordDigest="{1}", Nonce="{2}", Created="{3}"'.format(username, digest, base64.b64encode(nonce), created)


def makePost(link, title, summary):
    return post%(link, title, summary+"...")


# f = cgi.FieldStorage()
# username = cgi.escape(f.getfirst("username", ""),True);
# password = cgi.escape(f.getfirst("password", ""),True)

# db = sqlite3.connect('/var/www/html/s1j-news/db/data.db', isolation_level='DEFERRED')
# c = db.cursor()
# if username and password:
# 	db.execute("insert into Test values ('%s', '%s')" % (username, password))
# 	db.commit()

# c.execute("select * from Test")
# temp = ""
# for a in c:
# 	temp += "%s %s <br>" % (a[0], a[1])

# if username != USERNAME or password != PASSWORD:

	# db = sqlite3.connect('data.db', isolation_level='DEFERRED')
	# db.execute("insert into Test values (%s, %s)"%(username, password))
	# db.commit()
	# a = "hogehoge


#     print login_page % temp.encode("utf-8")

# else:
#     sc=Cookie.SimpleCookie()
#     sc['login']="ok"
    # print sc
    # print "Location: http://0.0.0.0:8000/cgi-bin/entry.cgi\n\n"
# print "Content-Type: text/html"
# print ""
# print ""

# print yuruyuri
tmp = ""

req = urllib2.Request(hatena_url)
req.add_header("X-WSSE", create_wsse(hatena_id, hatena_password))
res = urllib2.urlopen(req)
data = res.read()

root = ET.fromstring(data)

for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
    link = escape(entry.findall("{http://www.w3.org/2005/Atom}link")[1].get("href"))
    title = escape(entry.find("{http://www.w3.org/2005/Atom}title").text).encode("utf-8")
    try:
        summary = escape(entry.find("{http://www.w3.org/2005/Atom}summary").text).encode("utf-8")
    except:
        summary = "no summary"
    # link,title,summary="hoge","fuga","foo"
    if not ("si" in title):
        tmp += makePost(link, title, summary)

print page % tmp
