from pyquery import PyQuery as pq
from urllib.request import Request,urlopen
import os,codecs
import sys,re

import util.commonReg as m_reg


class basicParse:

	headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
	data = ''
	def __init__(self,url):
		self.url=url;

	def parser(self):
		req = Request(url=self.url,headers=self.headers)
		raw = urlopen(req).read()
		self.data =pq(raw)
	def getUrl(self):
		urlStack = self.data('a').text();
		for temp in urlStack.split(' '):
			print(temp)
		#raise urlStack

	def __urlRegex(string):
		pattern ="http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
		
		
def main():
	test=basicParse('https://www.ptt.cc/bbs/Shadowverse/M.1497623782.A.DE3.html')
	test.parser()
	
	test.getUrl()

if __name__=='__main__':
	main()	    		
