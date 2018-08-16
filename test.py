#!/usr/bin/python
# -*- coding: UTF-8 -*-# enable debugging

import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html;charset=utf-8")
print("")
print("Hello World!")
print('<a href="/test.py?x=2"><button>press</button></a>')
args = cgi.FieldStorage()
for i in args.keys():
    print (args[i].value)
    print (i)