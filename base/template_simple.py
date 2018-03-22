#!/usr/bin/env python
# -*- coding = utf-8 -*-

## 转换说明符的使用， %(xxx)s
## 使用HTML 作为实例

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
