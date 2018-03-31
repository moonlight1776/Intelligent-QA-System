# -*- coding: utf-8 -*-
#作者：Wang Feihong
#python 版本：3.6
#更新时间 2018/3/18
import re
import os
from tqdm import tqdm
from bs4 import BeautifulSoup

def del_tag(strings):
	dr = re.compile(r'<[^>]+>',re.S)
	if type(strings) == type([]): 
		strs = []
		for string in strings:
			string = str(string)
			strs.append(s)
		return strs
	else:
		strings= str(strings)
		s = dr.sub('',strings)
		return s


path = '/home/wangfeihong/桌面/support.huaweicloud.com/'

files = os.listdir(path)

for file in tqdm(files):
	data = {}	
	f = open(path + file,mode = 'r')
	text = f.read()
	print(file) 	
	if not 'developer' in file:
		elements = soup.select('.help-link')
		h1s = soup.select('h1')
		t = del_tag(elements)
		if "上一篇" in text:
			t.remove(t[len(t)-1])
		if "下一篇" in text:
			t.remove(t[len(t)-1])
		ele = soup.select('.topictitle1')
		title = del_tag(ele)
		if len(title) == 1:
			data['title'] = title[0]
			t.append(data['title'])
		else:
			data['title'] = 'null'
		data['desc'] = t
		
		soup = BeautifulSoup(str(details),'lxml')
		if len(descs) == 0:
			h1 = soup.h1
			siblings = []
			if len(h1) > 0:
				for s in h1.next_siblings:
					siblings.append(s)
			h4s = soup.select('h4')
			h3s = soup.select('h3')
			hs = h3s + h4s
			qas = []
			
			dls = soup.select('dl')
			if len(dls) > 0:
				for dl in dls:
					for s in dl.next_siblings:
						if not s.isspace:
							soup2 = BeautifulSoup(str(dl),'lxml')
							dts = soup2.dt
							dds = soup2.select('dd')
							dds = del_tag(dds)
							qas.append({'question':del_tag(dts),'answer':del_tag(s)}) 
			data['qas'] = qas						
			print(data)




	# developer
	else:
		soup = BeautifulSoup(text,'lxml')
		details = soup.select('#content')
		soup = BeautifulSoup(str(details),'lxml')
		descs = soup.select('.crumbs')
		titles = soup.select('span')
		if len(descs) == 0:
			h1 = soup.h1
			siblings = []
			if len(h1) > 0:
				for s in h1.next_siblings:
					siblings.append(s)
			h4s = soup.select('h4')
			h3s = soup.select('h3')
			h1s = soup.select('h1')
		
					
			data['qas'] = qas						
			data['title'] = del_tag(soup.select('.poster-caption'))[0]
			data['desc'] = data['title']
		else:
			pass
			# print(file)
			# texts = soup.select('.text')
			# desc = descs[0].get_text()
			# data['desc'] = desc
			# data['title'] = del_tag(titles[0])
			# data['qas'] = {'question':desc,'answer':del_tag(texts[0])}
# print(data)
