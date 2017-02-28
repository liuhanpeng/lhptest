#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib2
#使用get请求
#选择入口
if __name__ == '__main__':
    #设置header头部及url地址
    url = 'https://www.baidu.com'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    request = urllib2.Request(url=url,headers=headers)
    #发送请求和接收响应
    response = urllib2.urlopen(request)
    print response.read()