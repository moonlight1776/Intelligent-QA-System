# -*- coding: utf-8 -*-
#作者：Zhang Qinyuan
#python 版本：3.6
#更新时间 2018/3/18
import jieba.posseg as pseg

#def title_changing(sentence):
#	words = pseg.cut(sentence)
#	for word, flag in words:
#		
	words = pseg.cut(sentence)
#	i = 0
#	v = 0
	word_list = []
	for 
	for x in word_list:
		print(x, end = '')

def single_info_line_changing(sentence):
	words = pseg.cut(sentence)
	word_list = []
	for word, flag in words:
		if flag == 'v':
			print(word + '什么？')
			break
		print(word, end = '')

single_info_line_changing("阿里云也提供了API接口方便您管理云服务器ECS")
