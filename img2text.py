#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'这是实验楼的一个教学项目,将图片转换为字符画的形式'

__author__ = 'Engine'

from PIL import Image
import argparse

# 定义了一个解析器,用于命令行输入参数处理
parser = argparse.ArgumentParser()

parser.add_argument('file')
parser.add_argument('-o', "--output") # 指定输出文件
parser.add_argument('--width', type = int, default = 80) # 指定字符画的宽度
parser.add_argument('--height', type = int, default = 80)# 指定字符画的长度

# 获取参数
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

# 定义字符串,用于替代像素
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 将灰度映射到字符上
def get_char(r, g, b, alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    # 灰度计算公式
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    
    # 实现单个像素灰度与字符的映射 
    return ascii_char[int(gray*length/(256.0+1))]

if __name__ == "__main__":

    im = Image.open(IMG)
    im = im.resize((WIDTH, HEIGHT),Image.NEAREST)

    txt = ""

    # 遍历像素点,并转换
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    print(txt)

    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open("output.txt", 'w') as f:
            f.write(txt)
