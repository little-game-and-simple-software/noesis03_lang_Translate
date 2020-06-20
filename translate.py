# -*- coding: utf-8 -*-
import os
file=open("201.iet",'r',-1,"utf-8")
lines=file.readlines()
index=1

for line in lines:
    #print(index)
   # tmp_char=line[index]
    if "t" in line:
        print("当前行")
        print(line)
        t_pos=line.find("t")
        print("t在当前行的位置"+str(t_pos))
        print("t的下一个字符"+str(line[t_pos+1]))
        s=input()
        if s=="y":
            pass
        else:
            break
    index+=1
           
file.close()
#config.read("201.iet","utf-8")
