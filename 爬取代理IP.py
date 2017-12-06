import urllib.request
from bs4 import BeautifulSoup
import socket
import telnetlib

def getProxyIp():             #得到代理ip和检测
	proxy=[]
	head={}
	head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
	for i in range(1,5):
		url='http://www.xicidaili.com/nn/'+str(i)
		req=urllib.request.Request(url,headers=head)
		response=urllib.request.urlopen(req)
		html=response.read().decode('utf-8')
		soup=BeautifulSoup(html,"lxml")                     
		tr=soup.findAll("tr")        #找出所有的tr
		for x in range(1,len(tr)):
			ip=tr[x]
			td=ip.findAll("td")      #找出tr中的td
			ip_temp=td[1].contents[0]+"\t"+td[2].contents[0]  #把第一个td（ip）和第二个td（端口）取出来
			
			try:                      #检测代理ip
				telnetlib.Telnet(td[1].contents[0],port=td[2].contents[0],timeout=3)
			except:
				ip_telnet=ip_temp+"  connect failed"
			else:	
				ip_telnet=ip_temp+"  success"
			print(ip_telnet)
			proxy.append(ip_telnet)
			
	return proxy
	
def save(proxy):          #保存代理ip
	f=open("ip.txt","w")
	for i in range(0,len(proxy)):
		f.write(proxy[i]+'\n')
		
	f.close()
	
if __name__ == '__main__':
	proxy=getProxyIp()
	save(proxy)