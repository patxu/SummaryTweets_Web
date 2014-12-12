#!/usr/bin/python
"downloadHyp"
import cgitb; cgitb.enable()
import os
import cgi

form = cgi.FieldStorage()

os.chdir('/net/tahoe3/ifeng/Documents/')

if form.getvalue("filename"):
	filename = form.getvalue("filename")
	
print "Content-Type: application/octet-stream"
print "Content-Disposition: attachment; filename=%s" % filename
print 

fo = open(filename, "rb")

str = fo.read();
print str

fo.close()

#mfc = subprocess.call(['./featurize.sh'])
#hyp = subprocess.call(['./recognize.sh'])