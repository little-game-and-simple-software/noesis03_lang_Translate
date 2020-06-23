# -*- coding: utf-8 -*-
import os
import sys
import pyperclip
def trans(filepath):
    print("开始处理文件 ", filepath)
    with open(filepath, "r", encoding="utf8") as fr, open("%s.trans" % filepath, "w", encoding="utf-8") as fw:
        index = 1 
        for line in fr:
            print(index, "行: ", line)
            newline = line
            tt = line.split('text=')
            if len(tt) > 1:
                zz = tt[1].split('"')
                my_c=pyperclip.copy(str(zz))
                if len(zz) > 1:
                    s = input("请翻译: " + zz[1] + " =>")
                    if len(s) > 0:
                        zz[1] = s
                        tt[1] = '"'.join(zz)
                        newline = 'text='.join(tt)
                        print("翻译结果: " , newline)
                        print("------复制原文内容到剪贴板------")
                        print(my_c)
            fw.write(newline)
            index += 1
    print(filepath, "文件处理完成, 总行数：", index)

def main():
    path = '.'
    if len(sys.argv) > 1 :
        path = sys.argv[1]
    print("开始翻译, 参数: ", path) 
    if os.path.isdir(path):
        print("扫描目录下的iet文件")
        for f in os.listdir(path):
            if f.endswith('iet'):
                trans(os.path.join(path, f))
            else:
                print(f, " 非iet文件")
    else:
        if path.endswith('iet'):
            trans(path)
        print("输入文件非iet")
    print("完成！")

main()
