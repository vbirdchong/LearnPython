#!/usr/bin/env python
# coding: utf-8

# 第一行指代这是一个python 程序
# 第二行指 用UTF-8编码读取代码

### 从 mylibhello 中load
##import mylibhello
##
##h = mylibhello.Hello()
##h.sayHello()


# 用另一种方法加载 Hello 这个类

from mylibhello import Hello

h1 = Hello()
h1.sayHello()
