#encoding: utf-8
import re
import sys
import html
import pickle

"""
<font size=6 color=red>怀乡病</font>
<br>
<font  size=6 color=blue>hejmveo；nostalgio；hejmsopiro</font>
</>
"""

pattern1 = '\<font[^<>]*?color\=red[^<>]*?\>(.+?)\</font\>'
pattern2 = '\<font[^<>]*?color\=blue[^<>]*?\>(.+?)\</font\>'

d = {}
in_file = sys.argv[1]
with open(in_file, 'rb') as f, open('mydict.txt', 'w+b') as write_f:
    lines = f.readlines()
    lines = list(map(lambda x: x.strip(), lines))
    lines = list(filter(lambda x: len(x) > 0, lines))
    i = 0
    word1 = None
    word2 = None
    word_groups = []
    while 1:
        if word1 is None:
            o1 = re.search(pattern1, lines[i].decode('utf-8'))
            if o1:
                word1 = o1.group(1)
        else:
            o2 = re.search(pattern2, lines[i].decode('utf-8'))
            if o2:
                word2 = o2.group(1)
                word1 = html.unescape(word1)
                word2 = html.unescape(word2)
                word_group = [word1, word2]
                word_groups.append(word_group)
                if re.search('[a-z,A-Z]', word1[0]) is None:
                    print(word1)
                    print(word2)
                    d[word1] = word2
                word1 = None
        i += 1
        if i + 1 > len(lines):
            break
    print(len(d))
    pickle.dump(d, write_f)






