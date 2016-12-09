# -*- coding:utf-8 -*-
import collections
A = collections.OrderedDict()
while True:
    try:
        log = raw_input().strip("").split("\\")
        name = log[-1]
        if log == ['']:
            break
        A[name] = A.get(name,0) + 1
    except:
        break

lis = sorted(A.items(),key = lambda x:x[1],reverse=True)

count = 0
for key in lis:
    if count > 7:
        break
    count += 1
    if len(key[0].split(' ')[0]) > 16:
        print key[0].split(' ')[0][-16:], key[0].split(' ')[1], key[1]
    else:
        print key[0].split(' ')[0], key[0].split(' ')[1], key[1]