#!/usr/bin/python
# -*- coding: UTF-8 -*-# enable debugging

import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html;charset=utf-8")
print("")

print ("""
<html>
	<head>
		<meta charset="utf-8"/>
		<link type="text/css" rel="stylesheet" href="css.css"/>
		<title>Markiis</title>
		<style>
			p {font-size:1.5em}
		</style>
	</head>
	<body style="text-align:center; font-size:1.5em">
		<div style="border:1px solid black; padding:5px; margin:5px">
			<p> LAHTI KERIMISNUPUD </p>
			<a href="/?kerimine=jah&suund=lahti"> <button style="font-size:1.5em"> keri lahti </button> </a>
			<a href="/?kerimine=pooleldi&suund=lahti"> <button style="font-size:1.5em"> keri pool lahti </button> </a>
			<a href="/?kerimine=stopp&suund=stopp"> <button style="font-size:1.5em"> peata </button> </a>
		</div>
		<div style="border:1px solid black; padding:5px; margin:5px">
			<p> KINNI KERIMISNUPUD </p>
			<a href="/?kerimine=jah&suund=kinni"> <button style="font-size:1.5em"> keri kinni </button> </a>
			<a href="/?kerimine=stopp&suund=stopp"> <button style="font-size:1.5em"> peata </button> </a>
		</div>
		<div style="border:1px solid black; padding:5px; margin:5px">
			<p> OLEK </p>
""")
olekuFail = open("olek.txt", "r")
aeg = olekuFail.readline()
liikumisFaas = olekuFail.readline()
vool = olekuFail.readline()
saadudOlek = olekuFail.readline()
olekuFail.close()

print("<p> aeg: " + aeg + "</p>")
print("<p> liikumisfaas: " + liikumisFaas + "</p>")
print("<p> vool: " + vool + "</p>")
print('<a href="/?kerimine=olek&suund=jhdfbgjhfg"> <button style="font-size:1.5em"> tahan uut olekut </button> </a>')
print("</div>")




print ('<div style="border:1px solid black; padding:5px; margin:5px">')

print ("<p> debug kast </p>")

args = cgi.FieldStorage()
for i in args.keys():
    print ("<p>" + i + " = " + args[i].value + "</p>")

print ("<p> saadud olek: </p>")
print ("<p>" + saadudOlek + "</p>")
print("</div>")

print ("""
	</body>
</html>
""")
if (len(args.keys()) != 0):
	buffer = open("buffer.txt", "w")
	buffer.write(args["kerimine"].value)
	buffer.write("\n")
	buffer.write(args["suund"].value)