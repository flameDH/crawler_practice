import re

def basicfindReg(rawData,pattern):
	pattern=pattern;
	urls=re.findall(pattern,rawData)
	return urls

def basicMatch(rawData,pattern):
	pattern = pattern
	url=re.findall(pattern,rawData)
	return urls	

def findUrlReg(rawData):
	pattern="http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
	urls=re.findall(pattern,rawData)
	return urls

def checkUrlReg(rawData):
	a=123	

def main():
	b=456
if __name__=="__main__":
	main()
