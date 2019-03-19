# Brian Sheridan & Craig Calvert 
# CST 205
# Lab 16 

import urllib.request
import re
# open Webpage, read and decode wti utf-8
webPage = (urllib.request.urlopen("https://www.npr.org/sections/news/").read()).decode('utf-8')
#open output file for writing 
output = open("headline.html","w")
# find all occurences of headlines.
instance = re.findall(r'alt="(.*?)"',str(webPage))
# output to html file
for i in instance:
    output.write("<p>"+ i)
#close file
output.close()
