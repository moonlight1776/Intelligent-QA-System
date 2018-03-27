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
			s = dr.sub('',string)
		

path = '/home/wangfeihong/桌面/support.huaweicloud.com/'

files = os.listdir(path)

for file in tqdm(files):
	da
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
	
					siblings.append(s)
			h4s = soup.select('h4')
			h3s = soup.select('h3')
			h1s = soup.select('h1')
			hs = h1s + h3s + h4s
			qas = []
			if len(hs) > 0:
				for h in hs:
					for s in h.next_siblings:
						if not s.isspace:
							qas.append({'question':del_tag(h),'answer':del_tag(s)})
			dls = soup.select('dl')
			
			
			# print(file)
			# texts = soup.select('.text')
			# desc = descs[0].get_text()
			# data['desc'] = desc
			# data['title'] = del_tag(titles[0])
			# data['qas'] = {'question':desc,'answer':del_tag(texts[0])}
			# print(data)

