#!/usr/bin/python
"""TEST CGI""" 

import cgitb; cgitb.enable()
import tf_idf
import cgi

print "Content-type: text/html"

print "<html>"
print "<head>"
print "<title>Upload Wav"
print "</title>"

print "</head><body style=\"padding: 20px;\">"

form = cgi.FieldStorage()

if "textfile" in form:
    fileitem = form["textfile"]
    if fileitem.file:
    	#check if wav file
    	print "<p>Is file</p>"
    	#check directory

print "<h2>Upload wav file: <input type=\"file\" name=\"textfile\"/></h2>"

print "<input type=\"submit\" value=\"Submit\"></form><p>"
print "</div>"

print "</body></html>"