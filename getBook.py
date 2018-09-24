#！/usr/bin/env python3
#coding: utf-8
'''
# =============================================================================
#      FileName: getBook.py
#          Desc: bookschina团购推荐
#        Author: jianghao
#         Email: mail@jianghao.tech
#      HomePage: http://www.github.com/s-h
#       Version: 0.0.1
#    LastChange: 2018-09-23 20:59:36
#       History:
# =============================================================================
'''
import  requests
from bs4 import BeautifulSoup
url = "http://tuan.bookschina.com"
headers ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
r = requests.get(url, headers=headers, timeout=10)
html = r.text
soup = BeautifulSoup(html, "html.parser")
for h2 in soup.find_all('h2'):
    li = h2.parent
    title = li.h2.get_text()                          #书名

    bookName = li.find(class_="bookName")
    tag = bookName.a.get('href')
    description = bookName.a.get('title')               #描述
    
    price = li.find(class_="price")
    salePrice = price.find(class_="salePrice").get_text()   #优惠价格
    salequantity = price.find(class_="salequantity").get_text() #购买人数

    otherInfo = li.find(class_="otherInfor") 
    fixedPrice = otherInfo.find(class_="dingjia").get_text()   #定价
    discount = otherInfo.find(class_="zhekou").get_text()   #折扣

    #print('书名 %s,优惠价格 %s,购买人数 %s,定价 %s, 折扣 %s \n %s' % title, salePrice, salequantity, fixedPrice, discount, description )

    print(title)
    print(tag)
    print(description)
    print(salePrice)
    print(salequantity)
    print(fixedPrice)
    print(discount)
    print("----")

