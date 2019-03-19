#Lab16
#Kevin Bentley, Samuel Pearce
#CST 205

import urllib2
import re

url = 'https://news.google.com/?hl=en-US&gl=US&ceid=US:en'

f = urllib2.urlopen(url)
html = f.read()
info  = re.findall(r'<span>(.*?)</span>', html)
headers = []
#Loop that takes the information from headings and stores it into headers
i = 0
while i < 10:
  headers.append(info[i])
  i += 1
#Calls makePage and sends the list of 10 items stored in headers
makePage(headers)

def makePage(heads):
  file = open(pickAFile(), "wt")
  
  
  html_str = """
  <html>
  <head><title>I made this page with Python!</title>
  </head>
  <body>
  <h1>News Updates from Google News!</h1>
  <h2>%s</h2>
  <h2>%s</h2>
  <h2>%s</h2>
  <h2>%s</h2>
  <h2>%s</h2>
  <h2>%s</h2>
  <h2>%s</h2>
  <h2>%s</h2>
  <h2>%s</h2>
  <h2>%s</h2>
  </body>
  </html> """ %(heads[0],heads[1],heads[2],heads[3],heads[4],heads[5],heads[6],heads[7],heads[8],heads[9])
  
  
  file.write(html_str)
  file.close()

