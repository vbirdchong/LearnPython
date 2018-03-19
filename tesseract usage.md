## 验证码识别

对于验证码，我们可以通过ORC的开源库tesseract-orc来识别图中的内容，然后在python中使用pytesseract来调用它，获取正确的内容。

### tesseract-orc安装方法

1. tesseract-orc 下载地址如下：

https://github.com/tesseract-ocr/tesseract/wiki/4.0-with-LSTM#400-alpha-for-windows

2. 在安装的过程中，可以选择语言包，这样就可以对中文的识别进行支持。Additional language data 中可以选择简体和繁体

3. 安装完毕后，在环境变量中添加刚才的安装目录，如：C:\Program Files (x86)\Tesseract-OCR，将其添加至Path中

4. 设置TESSDATA_PREFIX全局属性，不然会报以下错误。在系统环境变量中新增如下内容

```
错误信息：
pytesseract.pytesseract.TesseractError: (1, u'Error opening data file \\Program Files (x86)\\Tesseract-OCR\\eng.traineddata Please make sure the TESSDATA_PREFIX environment variable is set to your "tessdata" directory. Failed loading language \'eng\' Tesseract couldn\'t load any languages! Could not initialize tesseract.')

变量添加：
TESSDATA_PREFIX，变量值设置为C:\Program Files (x86)\Tesseract-OCR
```

5. 检查安装结果，如果能正常查询版本，那么安装成功
```
H:\>tesseract -v
tesseract 4.00.00alpha
 leptonica-1.74.1
  libgif 4.1.6(?) : libjpeg 8d (libjpeg-turbo 1.5.0) : libpng 1.6.20 : libtiff 4
.0.6 : zlib 1.2.8 : libwebp 0.4.3 : libopenjp2 2.1.0
```

### pytesseract 安装

直接 pip install pytesseract 即可


### 使用

我们使用以下图片来进行试验。

![image](http://img.blog.csdn.net/20180209094145460)

```
测试结果
>>> from PIL import Image
>>> import pytesseract
>>> img = Image.open('1.png')
>>> img
<PIL.PngImagePlugin.PngImageFile image mode=P size=435x116 at 0x2E06D50>
>>> img = img.convert('L')
>>> img
<PIL.Image.Image image mode=L size=435x116 at 0x2E06FD0>
>>> pytesseract.image_to_string(img)
u'1 8 6 4 8 2'
>>>
```
