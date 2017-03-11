#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author: lhp
# Date: 2017/3/11
# Description:This is a python script that is used to compile other scripts.
import py_compile
import sys
py_compile.compile(sys.argv[1])
