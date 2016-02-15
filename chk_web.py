import time
import urllib.request
from urllib import *
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import pycurl
import os
import socket
from color import *

def getWebtime():
    c=pycurl.Curl()
    indexfile=open(os.path.dirname(os.path.realpath(__file__))+"/content.txt","wb")
    c.setopt(c.URL,i)
    #c.setopt(c.VERBOSE,1)#显示头文件具体内容
    c.setopt(c.ENCODING,"gzip")
    c.setopt(c.USERAGENT,"Mozilla/5.0 (Windows NT 6.1; rv:35.0) Gecko/20100101 Firefox/35.0")
    c.setopt(c.WRITEHEADER,indexfile)
    c.setopt(c.WRITEDATA,indexfile)
    c.perform()
    webtime = str(c.getinfo(c.TOTAL_TIME)*1000)+" ms"
    indexfile.close()
    c.close()
    return webtime

def getWebip(domain):
    webaddr = socket.getaddrinfo(domain,'http')[0][4][0]
    return webaddr



def getTime():
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

def getHtmlcode(url):
    try:
        header = {'User-Agent':'Chrome'}
        page = urllib.request.Request(url,None,header)
        response = urllib.request.urlopen(page)
        code = response.getcode()
        return code
    except urllib.error.HTTPError:
        code = '503'
        return code

def chkCode():
    global x
    global i
    for i in url:
        domain = i.split("://")[1]
        code = str(getHtmlcode(i))
        print('检查时间：' + getTime()+" "+ i +" 访问状态："+ code)
        print('加载用时： ' + getWebtime())
        print('当前IP地址：' + getWebip(domain))
        if i == 'http://www.primegene.com.cn':
           xy = l[0]
           if code != str(200):
               x = xy + '网址访问告警'
               errSendmail()
               clr.print_red_text('请重启服务器！！！')
        elif i == 'http://www.primegene.com':
            xy = l[1]
            if code != str(200):
               x = xy + '网址访问告警'
               clr.print_red_text('请重启服务器！！！')
               errSendmail()
        

def errSendmail():
    #global x
    sender='hjgood@163.com'
    receivers=('hjgood@163.com','itsupport.cn@bio-techne.com','Justin.Lin@bio-techne.com')
    #receivers=('hjgood@163.com','itsupport.cn@bio-techne.com')

    subject = x
    smtpserver = 'smtp.163.com'
    username = 'hjgood@163.com'
    password = '3mibms1981'

    msg = MIMEText('<h1>请注意,需重启服务器。</h1>','html','utf-8')
    msg['Subject'] = subject
    
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login(username,password)
    for receiver in receivers:
        smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
                      
            
if __name__ =='__main__':
    url = ("http://www.primegene.com.cn","http://www.primegene.com")
    l = ('中文','英文')
    clr = Color()
    while True:
        clr.print_blue_text('==========================================================================')
        chkCode()
        clr.print_blue_text('==========================================================================')
        time.sleep(300)
    
