#!/usr/bin/env python

"""TEST CGI""" 

import cgitb; cgitb.enable()
import tf_idf
import cgi

print "Content-type: text/html"
print ""
print "<html><head>"
print "<title>Web Interface Summary Tweets"
print "</title>"
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"http://www.cs.dartmouth.edu/~patxu/styles/layout.css\">"
print "</head><body style=\"padding: 20px;\">"

print "<span id=header><h1><center>Summary Tweets</center></h1></span>"

form = cgi.FieldStorage()

textbox = form.getvalue("textbox", "")
#textfile = form["textfile"]
#if "textfile" in form:
	#textfile = form["textfile"] 
	#textfile = form.getvalue("textfile")

print "<div class=\"content\"><h1>Enter input</h1><p>"
print "<form action=\"summary.cgi\" method=\"post\">" #action is the name of the page?? 
print "<p>You may enter text as input or just a link to the article you wish to tweet.<p>"
print "<textarea rows=\"10\" cols=\"60\" name=\"textbox\">"
print cgi.escape(textbox)+"</textarea><p>"
#print "<h2>Or Upload a file: <input type=\"file\" name=\"textfile\"/></h2>"
#print "*.txt files only<p>"

print "<input type=\"submit\" value=\"Submit\" float=\"right\"></form><p>"
print "</div>"

program = tf_idf.tfidf()
output = ""
#print textfile
#if textfile.file:
	#text = textfile.file.read()
	#print text
	#textbox = text #sets textbox to whatever is uploaded 

#textbox = textbox.lower()

print "<div class=\"content\">"
print "<h1>Results</h1><p>"
print "<p>Compressed results here.<p>"
if textbox != "":
	text = program.read_input_text(textbox)
	scores = program.tf_idf(text)
	summary2 = program.total_sent_score(text, scores)
	#program.compressor.simple_drop(summary2, text, scores)

	compressed = program.compressor.compress_sentences(summary2)
	if program.has_url(): length = 134 - 23 #-23 for link+space(twitter condenses all links to max 22 characters)
	else: length = 134
	output = program.output_sentences(compressed, length)
	print "<textarea rows=\"10\" cols=\"60\" float=\"right\" name=\"output\">"
	cgi.escape(output)
	print cgi.escape(output)+"</textarea><p>"
	output = output.replace(" ", "%20")
print "<p>Use the twitter bird to tweet your result!<p>"
print "<a class=\"twitter-hashtag-button\" href=\"https://twitter.com/intent/tweet?button_hashtag=CS73&text="+output+"\">"
print "<img src=\"http://upcity.com/blog/wp-content/uploads/2014/02/twitter-bird-white-on-blue-xl.png\" align=\"center\" width=\"20%\" height=\"auto\">"
print "</a>"

print "</div>"
print "<div style=\"clear: both;\"></div>"
print "<div class =\"copyright\">"
print "<p> <p></div>"
print "<div class =\"footer\" id = \"footbox\">Authored by: Irene Feng, Orestis Lykouropoulos, and Patrick Xu </div>"
print "</body></html>"
