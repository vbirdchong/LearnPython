#!/usr/bin/env python
# -*- coding = utf-8 -*-

## ת��˵������ʹ�ã� %(xxx)s
## ʹ��HTML ��Ϊʵ��

templtate = '''<html>
<head><title>%(title)s</title></head>
<body>
<h1>%(title)s</h1>
<p>%(text)s</p>
</body>'''

data = {
    'title' : 'My home page',
    'text'  : 'Welcome to my home page'
}

print templtate % data
