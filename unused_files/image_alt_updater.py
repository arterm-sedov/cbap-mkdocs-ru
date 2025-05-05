#!/usr/bin/env python3
import mysql.connector
from getpass import getpass
import html
from html.parser import HTMLParser
import bs4
class myparser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		if tag == 'img':
			print("IMG tag with attrs %s\n" % repr(attrs))

import os.path

conn = mysql.connector.connect(database='phpkbv9',
	user=input("User:\n"),
	password=getpass("Password for phpkbv9:\n"))
if conn:
	c = conn.cursor()
	c.execute("SELECT article_id, article_content from phpkb_articles")
	pages = 0
	images = 0
	for id, content in c.fetchall():
		print("ID: %s" % id)
		if not os.path.exists("article_content/%d_before.html" % id): continue
		with open("article_content/%d_before.html" % id) as b:
			
			p = bs4.BeautifulSoup(html.unescape(b.read()), 'html.parser')
			found = False
			for i in p.find_all('img'):
				if i.get('alt') == '':
					found = True
					desc =  i.parent.parent.find('p', 'caption')
					if desc:
						images += 1
						i['alt'] = desc.get_text()
			if found:
				with open("article_content/%d_after.html" % id, "w+") as b:
					b.write(html.escape(str(p)))
				pages += 1
				c.execute("UPDATE phpkb_articles set article_content=%s where article_id=%s", (html.escape(str(p)), id))
				conn.commit()
				print("%d Images updated in %d pages" % (images, pages))

