#!/usr/bin/env python
# coding:utf-8

from PIL import Image
import argparse

# 命令行输入参数处理
parser = argparse.ArgumentParser()

# 输入文件
parser.add_argument('file')

# 输出文件
parser.add_argument('-o', '--output')	

# 输出字符画 宽
parser.add_argument('--width', type = int, default = 80)

# 输出字符画 高
parser.add_argument('--height', type = int, default = 80)


args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(r, b, g, alpha = 256):
	if alpha == 0:
		return ' '

	length = len(ascii_char)
	# 灰度值换算
	gray = int(0.2126 * r + 0.7125 * g + 0.0722 * b)

	unit = (256.0 + 1) / length
	return ascii_char[int(gray/unit)]


def main():
	im = Image.open(IMG)
	im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

	txt = ""

	for i in range(HEIGHT):
		for j in range(WIDTH):
			txt += get_char(*im.getpixel((j,i)))
		txt += '\n'

	print txt


if __name__ == '__main__':
	main()





