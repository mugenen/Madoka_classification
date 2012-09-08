#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import collections
reload(sys)
sys.setdefaultencoding('utf-8')

import MeCab
mecab = MeCab.Tagger('-Ochasen')
names = { 'homura' : 1,
          'kyoko' : 2,
          'kyube' : 3,
          'madoka' : 4,
          'mami' : 5,
          'sayaka' : 6 }

words = {}
num = 0

result = collections.defaultdict(list)

for i in names.keys():
    file = './data/' + i + '.txt'
    for line in open( file, 'r' ):
        attrs = collections.Counter()
        line = line.strip().rstrip()
        n = mecab.parseToNode( line )
        surface = []
        while n.next:
            surface.append(n.surface)
            n = n.next
        for j, k in enumerate(surface):
            if k not in words:
                words[k] = num
                num += 1
            id = words[k]
            attrs[id] += 1
#        for j, k in enumerate(surface[:-1]):
#            k = (k, surface[j + 1])
#            if k not in words:
#                words[k] = num
#                num += 1
#            id = words[k]
#            attrs[id] += 1

        text = ''
        text += str(names[i]) + ' '
        for ak in sorted(attrs.keys()):
            text += str(ak) + ":" + str(attrs[ak]) + ' '
        result[i].append(text)

for i in result.keys():
    if i == 'homura':
        for l in result[i]:
            print l
    else:
        for l in result[i]:
            print str(-1) + l[1:]
    with open('ff.txt', 'w') as fi:
        for k, v in sorted(words.items(), key = lambda x: x[1]):
            fi.write(k + ', ' + str(v) + '\n')

