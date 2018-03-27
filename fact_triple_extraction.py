# -*- coding: utf-8 -*-
#作者：Wang Feihong
#python 版本：3.6
#更新时间 2018/3/18
import codecs   
import re 
from pyltp import SentenceSplitter  
from pyltp import Segmentor  
from pyltp import Postagger  
from pyltp import NamedEntityRecognizer  
  
#
    postagger = Postagger()  
    postagger.load('/home/wangfeihong/桌面/ltp_data/pos.model')  
    posttags=postagger.postag(words)  #词性标注  
    postags = list(posttags)  
    postagger.release() #释放模型  
    #print type(postags)  
    return postags  
  
#命名实体识别  
def ner(words,postags):  
    print('命名实体开始！')  
    recognizer = NamedEntityRecognizer()  
    recognizer.load('/home/wangfeihong/桌面/ltp_data/ner.model') #加载模型  
    netags = recognizer.recognize(words,postags) #命名实体识别  
    for word,ntag in zip(words,netags):  
        print(word+'/'+ ntag)  
    recognizer.release()   #释放模型  
    nerttags = list(netags)  
    return nerttags  
  
#新建一个txt文件保存命名实体识别的结果      
out_file = codecs.open('out_nerfile.txt','w',encoding='utf8')  
sents = sentence_splitter(news_list[0].encode('utf-8'))  
for sent in sents:  
    words=segmentor(sent)  
    tags = posttagger(words)  
    nertags = ner(words,tags)  
    for word,nertag in zip(words,nertags):  
        out_file.wr词组的各个词   
ner_list=[]  
phrase_list=[]
word_list=[]
for word in file_list:  
    # if(re.search('Ni$',word)):  
    word_list=word.split('/')
    if re.search(r'^S',word_list[1]):  
        ner_list.append(word_list[0])
        print('提取出的命名实体为：',word_list)
    elif re.search(r'^B',word_list[1]):  
        phrase_list.append(word_list[0]) 
        print('提取出的命名实体为：',word_list)
    elif re.search(r'^I',word_list[1]):  
        phrase_list.append(word_list[0])
        print('提取出的命名实体为：',word_list)
    else:  
        phrase_list.append(word_list[0])  
        # print('提取出的命名实体为：',word_list[0])
        #把list转换为字符串.  
        ner_phrase=''.join(phrase_list)  
        ner_list.append(ner_phrase)   
        phrase_list=[]   
# for ner in ner_list:  
#     print(ner)  
