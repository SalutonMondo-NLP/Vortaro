#encoding: utf-8

import pickle
import jieba
import requests
import pinyin


key = 'trnsl.1.1.20181128T061330Z.311f1dd648d5d8d6.5dc1a0d7f9c84fe99446fb4118c6cad694241039'
lang = 'zh-eo'

s = '''
计算机、软件、硬件、机电一体化产品开发、销售、安装，计算机软件技术开发、技术转让、技术咨询服务，场地租赁，计算机软、硬件租赁，CT机生产，物业管理，交通及通信、监控、电子工程安装，安防设施设计与施工，建筑智能化工程的施工，医用电子仪器设备批发、临床检验分析仪器批发，汽车零部件及配件、通讯系统设备的批发和零售，通讯终端设备的设计、技术开发、技术咨询、技术服务、测试及售后服务，多媒体智能支付终端设备、集成电路卡及集成电路卡读写机的研发、设计、生产、销售及售后服务，健康信息管理及咨询服务（以上经营项目不含诊疗），经营本企业自产产品及技术进出口业务和本企业所需的机械设备、零配件、原辅材料及技术的进口业务，但国家限定或禁止进出口的商品及技术除外。（依法须经批准的项目，经相关部门批准后方可开展经营活动。）
'''

ignores = {'，', '。', '）', '（', '；', ';', '(', ')', '、'}
skips = {'的'}

to_translate = set()

jieba.load_userdict('additional_fenci.txt')
all_text = []

ultra_segs = set()

with open('/Users/zdb/miniconda2/envs/python37/lib/python3.7/site-packages/jieba/dict.txt') as f1, open('additional_dict.txt') as f2:
    for each in f1:
        each = each.strip()
        if not each:
            continue
        text = each.split(' ', 1)
        ultra_segs.add(text[0])
    for each in f2:
        each = each.strip()
        if not each:
            continue
        text = each.split(' ', 1)
        ultra_segs.add(text[0])

with open('mydict.txt', 'rb') as f, open('additional_dict.txt') as dict_f:
    d = pickle.load(f)
    for each in dict_f:
        each = each.strip()
        if not each:
            continue
        word1, word2 = each.split(' ', 1)
        d[word1] = word2
    seg_list = jieba.cut(s)
    for seg in seg_list:
        seg = seg.strip()
        if seg in d:
            if seg in skips:
                continue
            if seg.isdigit():
                all_text.append(seg)
                continue

            print('seg hit', seg, d[seg])
            multiple_trans = d[seg].split(';')
            multiple_trans1 = d[seg].split('；')
            all_text.append(len(multiple_trans) > 1 and multiple_trans[0] or len(multiple_trans1) > 1 and multiple_trans1[0] or d[seg])
            pass
        else:
            all_text.append(seg)
            if seg and seg not in ignores:
                print('seg miss', seg)
                to_translate.add(seg)

print(' '.join(all_text))

with open('additional_dict.txt', 'ab') as f:
    for text in to_translate:
        if text not in ultra_segs:
            pinyin_text = pinyin.get(text, format="strip")
            s = text + ' ' + pinyin_text + '\n'
            s = s.encode('utf-8')
            f.write(s)
            f.flush()
            continue
        post_data = {'key':key, 'lang': lang, 'text': text}
        print('translate %s online' % text)
        r = requests.post('https://translate.yandex.net/api/v1.5/tr.json/translate', post_data)
        trans_data = r.json()
        trans_text = trans_data.get('text', [])
        if trans_text:
            s = text + ' ' + trans_text[0] + '\n'
            s = s.encode('utf-8')
            f.write(s)
            f.flush()
