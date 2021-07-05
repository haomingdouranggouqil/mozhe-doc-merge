import os
import re

#root = '1300-清'
root = input()

def getpathlist(filepath):
    pathlist = []
    for i,j,k in os.walk(filepath):
        return j

def gettxtlist(filepath):
    pathlist = []
    for i,j,k in os.walk(filepath):
        return k

def getpathnumber(pathlist):
    pathnumber = []
    for i in pathlist:
        pathnumber.append(int(i.split('-')[0]))
    return pathnumber

def gettruepath(pathlist):
    pathnumber = getpathnumber(pathlist)
    truepath = []
    pathdict = dict(zip(pathlist, pathnumber))
    correctdict = sorted(pathdict.items(), key=lambda d:d[1])
    for i in correctdict:
        truepath.append(i[0])
    return truepath


colums = getpathlist(root)
true_colu = gettruepath(colums)

md = root.split('-')[1] + '.md'
#fi = open('清.md', 'a', encoding='utf-8', errors='ignore')
fi = open(md, 'a', encoding='utf-8', errors='ignore')

for i in true_colu:
    path_name = root + '//' + i
    print(i.split('-')[1])
    fi.write('### '+i.split('-')[1] + '\n')
    txt = gettxtlist(path_name)
    true_txt = gettruepath(txt)
    for j in true_txt:
        txt_name = path_name + '//' + j
        print(j.split('-')[1][:-4])
        fi.write('#### '+j.split('-')[1][:-4] + '\n')
        ft = open(txt_name, 'r', encoding='utf-8', errors='ignore')
        txt_list = ft.readlines()
        for s in txt_list:
            if s == '\n':
                pass
            else:
                print(s)
                fi.write(s)
fi.close()
