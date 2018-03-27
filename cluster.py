# -*- coding: utf-8 -*-
#作者：Wang Feihong
#python 版本：3.6
#更新时间 2018/3/18
import re
from jieba import analyse



	# for word in wds.keys():'
			# if word in question_word:
		# 	w1[word] = wds[word]
		# print(w1)
	if 'a' in w1.values() and 'r' not in w1.values():
		for word in w1.keys():
			if w1[word] == 'a':
				keywords.append(word)
	else:		 
		for word in w1.keys():
			if w1[word] == 'r':
				keywords.append(word)
	return keywords
 
def question_type(text):
	if list(set(text).intersection(set(['何处','何地','哪儿','哪里','那儿','哪']))):
		return ('地点')
	if list(set(text).intersection(set(['何时','时候','哪天','哪年','月']))):
		return ('时间')
	if list(set(text).intersection(set(['人','谁']))):
	rds)
# print(questiontype)
keywords = analyse.extract_tags(text,topK=20, withWeight=False,allowPOS=['ns','n','vn','v','nr'])
print(keywords)




# words = pseg.cut("什么哪里?")
# dict = {}
# for word,flag in words:
# 	print(word)
# 	print(flag)
# 	dict[word] = flag
# # print(dict)
# keys = dict.keys()
# r = []
# for key in keys:
# 	if dict[key] == 'r':
# 		r.append(key)
# print(r)



