# Intelligent-QA-System
the knowledge base management base on NPL

词库需要自己用大量相关文档构建，文档越多，相关度越大，分词正确率越高，但仍不能保证100%的正确率。
做完分词和词性标注后。对问题进行分析。
        	  === 问题分类
          |
问题分析 ---=== 主题提取
	        |
	          === 关键词提取
问题分类是问句理解的必须步骤。
问题分类分为两种
1.基于规则的：
根据词性标注的结果，判断各种词序的顺序，句法
2.基于统计的：
用机器学习训练模型
暂时不知道两种效果如何，计划都做


关键词提取:
1.可以用jieba库：
https://www.cnblogs.com/zhbzz2007/p/6177832.html
1) 基于TF-IDF算法进行关键词抽取
2) 基于TextRank算法进行关键词抽取




引用

http://www.doc88.com/p-1465284404817.html

jieba库
    开发者可以指定自己自定义的词典，以便包含 jieba 词库里没有的词。虽然 jieba 有新词识别能力，但是自行添加新词可以保证更高的正确率
    用法： jieba.load_userdict(file_name) # file_name 为文件类对象或自定义词典的路径
    词典格式和 dict.txt 一样，一个词占一行；每一行分三部分：词语、词频（可省略）、词性（可省略），用空格隔开，顺序不可颠倒。file_name 若为路径或二进制方式打开的文件，则文件必须为 UTF-8 编码。
