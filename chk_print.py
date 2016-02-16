# -*- coding: utf-8 -*-
import urllib
import re
import urllib.request
from color import *


def brotherPrint(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:35.0) Gecko/20100101 Firefox/35.0'}
    #global weblink
    try:
        page = urllib.request.Request(urlbrother[0], None, header)
        response = urllib.request.urlopen(page)
        html = response.read().decode('utf-8')
        response.close()
        reg = u'(\u58a8\u7c89\u91cf\u4f4e)'
    #<td class="itemSpsFont">(No)</td>
        count = re.compile(reg)
        brotherchk = re.findall(count, html)
        return brotherchk[0]
    except IndexError:
        brotherchk = '墨粉量低'
        return brotherchk


def hpPrint(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:35.0) Gecko/20100101 Firefox/35.0'}
    try:
        page = urllib.request.Request(urlhp[0], None, header)
        response = urllib.request.urlopen(page)
        html = response.read().decode('utf-8')
        response.close()
    #reg = u'(\u6b63\u5e38\u0020)'
        reg = r'No'
        count = re.compile(reg)
        hpchk = re.findall(count, html)
        return hpchk[0]
    except IndexError:
        hpchk = 'Yes'
        return hpchk

def hpPrint4(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:35.0) Gecko/20100101 Firefox/35.0'}
    page = urllib.request.Request(urlhp4[0], None, header)
    response = urllib.request.urlopen(page)
    html = response.read().decode('utf-8')
    response.close()
    reg_b = u'(\u9ed1\u767d\u78b3\u7c89\u76d2)'
    count = re.compile(reg_b)
    hpchk = re.findall(count, html)
    

if __name__ == '__main__':
    global weblink
    clr = Color()
    urlbrother = ('http://192.168.18.30','Mfc-7850DN','192.168.18.30')
    urlhp = ('http://192.168.18.27/info_suppliesStatus.html?tab=Status&menu=SupplyStatus','P2015','192.168.18.27')
    urlhp4 = ('http://192.168.18.34/info_suppliesStatus.html?tab=Home&menu=SupplyStatus','M276n','192.168.18.34')
    
    if brotherPrint(urlbrother) == '墨粉量低':
        clr.print_red_text(urlbrother[1] + " 打印机硒鼓需要更换!!! " + urlbrother[2])
        
    else:
        print(urlbrother[1] + ' 打印机硒鼓容量正常 ' + urlbrother[2])
    #urlhp = ('http://192.168.18.31/info_suppliesStatus.html?tab=Home&menu=SupplyStatus','M202dw','192.168.18.31')
    if hpPrint(urlhp) != 'No':
        clr.print_red_text(urlhp[1] + " 打印机硒鼓需要更换!!! " + urlhp[2])
    else:
        print(urlhp[1] + ' 打印机硒鼓容量正常 ' + urlhp[2])
        
    input("")
