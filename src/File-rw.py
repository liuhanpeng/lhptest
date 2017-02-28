#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import os
#定义全局变量
setenfence = '''This is a test \
that will be used to read and write into file'''

#写入数据到文件
#打开文件
fw = open('test.txt','w')
#将变量值写入text.txt之中
fw.write(setenfence)
#关闭文件
fw.close()

#读取文件内容
#打开文件
fr = open('test.txt')
#读取文件
while True:
    line = fr.readline()
    if len(line) == 0:
        break
    print line
fr.close()
#5s后删除文件
time.sleep(5)
os.remove('test.txt')
