# Intelligent-QA-System
the knowledge base management base on NLP

智能问答系统分为两部分，一是知识库的构建（建立问题到答案的关系），建议问题的生成以方便后台增删查改。二是推理机，知识推理运用建立在知识库所存储的知识的基础之上的,不同的知识表达方式在一定程度上决定了特定的知识运用方式。

### 知识库

基于NLP 
想法是:每个答案有一个独有的 关键词数组 还应该有个属性比如人或者物体
知识字典 D 可用三元组表示如下:
D = ( O , T , E )
这里 O 表示对象, T 表示对象的分类即通常所说的词类, E 表示对象 O 的语义解释。
按照一些类似于决策树的算法，一步步筛选

### 建议问题的生成

我们目前将大部分说明类文档的肯定句分为以下三类进行建议问题生成：

1. 定义句：如“云服务器ECS是阿里云提供的一种基础云计算服务。”，这类句子定义了某种产品或者功能的意义或者价值。
2. 信息句：这类句子的主语为商家名或产品名，如“阿里云提供了Web服务页面。”，“ECS支持预付费和按量付费。”，这类句子提供了某些关于商家或产品的信息。
3. 指导句：这列句子的主语为“您”，“你”，“用户”等词汇，如“您可以根据业务需求和策略的变化自动调整ECS资源。”，这类句子指导用户去做某某件事。

其他类型尚待挖掘。

### 推理机

推理机针对当前问题的条件或已知信息，反复匹配知识库中的规则，获得新的结论，以得到问题求解结果。

要理解用户的问题，首先就要分词，对每个词进行分析
词库需要自己用大量相关文档构建，文档越多，相关度越大，分词正确率越高，但仍不能保证100%的正确率。
做完分词和词性标注后。对问题进行分析。

       	   	=== 问题分类
       		|           
     问题分析  ---    === 主题提取
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
1) 基于TF-IDF算法进行关键词抽取：
TF-IDF的主要思想就是：如果某个词在一篇文档中出现的频率高，也即TF高；并且在语料库中其他文档中很少出现，即DF的低，也即IDF高，则认为这个词具有很好的类别区分能力。TF-IDF在实际中主要是将二者相乘
2) 基于TextRank算法进行关键词抽取

经过实验发现jieba库的词库不能满足大部分的关键词提取。比如“什么东西最硬”提取出的关键词只有"什么"和“东西"。可取的是他的算法，不过词库需要我们自己去训了。


已做完的:问题分析-->问题分类(提取疑问词和关键词)-->确定答案类型:

先前想：建立疑问词词表，从词表中找疑问词，后来发现jieba库的词性标注还不错，通过一些规则正确率还行，暂时没有必要做疑问词词表

词性标注--从分出的词中提出存在于疑问词表中的词（可以是多个）--如果存在词性为r的词，则去除词性为a的词
例如：人有多重(并没有代词r)所以多是疑问词,什么人最多(什么人存在于疑问词表中，所以什么人是疑问词)
还有判断疑问词存在的顺序，如果存在多少，直接判定多少是疑问词等等

关键词提取--先用TF-IDF吧,知识库构建也用同一种算法，这样关键词应该对应得上



引用
http://www.doc88.com/p-111669478578.html
http://www.doc88.com/p-1465284404817.html

jieba库
    开发者可以指定自己自定义的词典，以便包含 jieba 词库里没有的词。虽然 jieba 有新词识别能力，但是自行添加新词可以保证更高的正确率
    用法： jieba.load_userdict(file_name) # file_name 为文件类对象或自定义词典的路径
    词典格式和 dict.txt 一样，一个词占一行；每一行分三部分：词语、词频（可省略）、词性（可省略），用空格隔开，顺序不可颠倒。file_name 若为路径或二进制方式打开的文件，则文件必须为 UTF-8 编码。
