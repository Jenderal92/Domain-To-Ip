#DOMAIN TO IP !!!
#!/usr/bin/python
# -*- coding: utf-8 -*
#JametKNTLS - h0d3_g4n - Moslem - Jenderal92 -Kiddenta
# Blog : https://www.blog-gan.org          
#DONATE ME :(
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614

from socket import gethostbyname
from urlparse import urlparse
from multiprocessing.dummy import Pool
from colorama import Fore


def ip(url):
	print (Fore.GREEN + "Get IP From: " + Fore.WHITE + url)
	try:
		if not urlparse(url).scheme:
			url = urlparse('http://'+url).netloc
		else: 
			url = urlparse(url).netloc
			open("Shin_IP.txt","a").write(str(gethostbyname(url))+"\n")
	except:
		pass

def Main():
	try:
		print (Fore.YELLOW + "DOMAIN TO IP " + Fore.WHITE)
		list = raw_input("\n\033[91mGive Me List\033[97m:~# \033[97m")
		pler = open(list, 'r').read().splitlines()
		prr = Pool(20)
		po = prr.map(ip, pler)
	except:
		pass

if __name__ == '__main__':
	Main()