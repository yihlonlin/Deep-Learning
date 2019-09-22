import jieba
# jieba.set_dictionary("Ex01/dict.txt.big")
import sys

import jieba.posseg as psg

jieba.load_userdict("userdict.txt")
jieba.add_word('劉懿珊')
jieba.add_word('許成名')

file = open('data.txt', 'r')

a = file.read()
print([(x.word, x.flag) for x in psg.cut(a)])
c = []
for x in psg.cut(a):
    if x.flag == "nr":
        ax = x.word
        #判斷在list裡人名有無出現過
        try:
            c.index(ax)
        except ValueError:
            c.append(ax)
print(c)
print(len(c))
