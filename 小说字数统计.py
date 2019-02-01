#!usr/bin/env python
# coding:utf8

import json

fr = open('hlm.txt',encoding="utf-8")

charaters = []
stat = {}

for line in fr:
	line = line.strip()
	
	if len(line) == 0:
		continue

	for x in range(0,len(line)):
		if line[x] in [' ','\t','\n','，','。','：','“','”','！','？','、','；','《','》','‘',':','【','】','〔','〕','[',']','/']:
			continue

		if not line[x] in charaters:
			charaters.append(line[x])

		if not line[x] in stat:
			stat[line[x]] = 0
		stat[line[x]] += 1

fw = open('result.json','w',encoding="utf-8")
fw.write(json.dumps(stat))
fw.close()

stat = sorted(stat.items(),key=lambda d:d[1],reverse=True)

for x in range(0,20):
	print (stat[x])

fw = open('result.csv','w',encoding="utf-8")
for item in stat:
	fw.write(str(item[0]) + ',' + str(item[1]) + '\n')
fw.close()

fr.close()
