#!/usr/bin/python
"""uploadWav"""

import cgitb; cgitb.enable()
#use cgitb.enable(display = 0, logdir = "/path") to see error logs - when live :) 
import os
import cgi
import subprocess 

print "Content-type: text/html"
print
print "<html><head>"
print "<title>Upload Wav"
print "</title>"
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"http://www.cs.dartmouth.edu/~ifeng/styles/ASR.css\">" #maybe move css file

print "</head><body style=\"padding: 20px;\">"

form = cgi.FieldStorage()
error = ""

print "<div><form action=\"uploadWav.cgi\" method=\"post\" enctype=\"multipart/form-data\">"
print "<h2>Upload wav file: <input type=\"file\" name=\"textfile\"/></h2>"
print "<input type=\"submit\" value=\"Submit\"></form>"

if "textfile" in form:
	filewav = form["textfile"]
	if filewav.file:
		#check if wav file
	    fileName,fileExtension = os.path.splitext(filewav.filename)
	    if fileExtension != '.wav':
	        error = "Extension incorrect. Please choose a .wav file"
	    else:
	        #print "<p>is a wav file"
	        try:
	            os.chdir('/net/tahoe3/ifeng/Documents/') #change to ~/data/webphonetics
	            download = open('asldkfjasdf','w')
	            o = open('/net/tahoe3/ifeng/Documents/' + filewav.filename, 'w') #change to ~/data/webphonetics/wav/
	            o.write(filewav.file.read())
	            o.close()
	            sox = subprocess.call(['sox', filewav.filename, '-r','16k', 'converted_'+filewav.filename,'channels','1']) #add 'wav/' to filewav.filename. 
	            #is it a hazard to overwrite the file? otherwise, before calling ./featurize, i would delete filewav anyway
	            os.remove(filewav.filename)

	            print "<form method=\"post\" action=\"http://www.cs.dartmouth.edu/cgi-bin/cgiwrap/ifeng/downloadHyp.cgi\" enctype = \"multipart/form-data\">"
	            print "<input type=\"hidden\" name=\"filename\" value=\"converted_"+filewav.filename+"\">"
	            print "<input type=\"submit\" value=\"Download File\"></form>"

	            #mfc = subprocess.call(['./featurize.sh'])
	            #hyp = subprocess.call(['./recognize.sh'])
	        except IOError:
	            error = "Error Reading File. Try again. You may need eto remove any whitespace or '/' characters from the file name."     #check directory
print "<span class=\"error\" name=\"error_msg\">"+error+"</span>" #can't move up? 

print "</div>"

print "</body></html>"