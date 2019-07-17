#encoding: utf-8
# 列出双向词典汉语词
# 列出汉语词库没有在词典里面的词

# 给出工商信息 分成尽量短的词 查找是否有缺的词
import os
import pickle
import re

import sh
import subprocess
# import collections
#
# ultra_segs = collections.()
#
# with open('/Users/zdb/miniconda2/envs/python37/lib/python3.7/site-packages/jieba/dict.txt') as f1:
#     for each in f1:
#         each = each.strip()
#         if not each:
#             continue
#         text = each.split(' ', 1)
#         ultra_segs.add(text[0])


clean_segs = []
status = 0

if os.path.exists('out/status.txt'):
    with open('out/status.txt', 'rb') as f:
        s = f.read()
        data = s.decode('utf-8')
        status = int(data)

with open('/Users/zdb/miniconda2/envs/python37/lib/python3.7/site-packages/jieba/dict.txt') as f1:
    for each in f1:
        each = each.strip()
        if not each:
            continue
        text = each.split(' ', 1)
        word = text[0]
        if not len(word) == 3:
            # dont consider word length longer than 4
            continue
        # if len(word) == 4:
        #     word1, word2 = word[0:2], word[2:]
        #     if word1 in ultra_segs and word2 in ultra_segs:
        #         print('4 length word split', word)
        #         continue
        clean_segs.append(word)

# not_in_words = []
# with open('mydict.txt', 'rb') as f, open('additional_dict.txt') as dict_f:
#     d = pickle.load(f)
#     new_d = {}
#     for each in d:
#         if re.search('[a-z,A-Z]', each[0]) is None:
#             new_d[each] = d[each]
#
#     for each in clean_segs:
#         if each not in new_d:
#             not_in_words.append(each)
#             # print(each)
#         else:
#             # print(each)
#             pass
#
#     print(len(not_in_words), 'not in', len(clean_segs))
#     print('dict has', len(new_d))


with open('out/hit.txt', 'ab') as hit_f, open('out/miss.txt', 'ab') as miss_f:
    for each in clean_segs[status:]:
        if len(each) == 1:
            continue
        value = subprocess.run('grep -irnI %s *.txt' % each, shell=True)
        if value.returncode == 0:
            hit_f.write(each.encode('utf-8') + b'\n')
        else:
            print(each)
            miss_f.write(each.encode('utf-8') + b'\n')
        status += 1
        print(status)
