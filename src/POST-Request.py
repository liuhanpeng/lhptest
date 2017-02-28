#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib
import urllib2
#使用post请求
#选择入口
if __name__ == '__main__':
    #设置header头部及url地址
    url = 'https://www.oschina.net/action/user/hash_login'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
    values = {'email':'1790912450@qq.com','pwd':'123456'}
    data = urllib.urlencode(values)
    request = urllib2.Request(url=url,data=data,headers=headers)
    #发送请求和接收响应
    response = urllib2.urlopen(request)
    print response.read()