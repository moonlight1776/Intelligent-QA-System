# Intelligent-QA-System
the knowledge base management base on NLP

智能问答系统分为两部分，一是知识库的构建（建立问题到答案的关系），建议问题的生成以方便后台增删查改。二是推理机，知识推理运用建立在知识库所存储的知识的基础之上的,不同的知识表达方式在一定程度上决定了特定的知识运用方式。

### 知识库

知识字典 D 可用三元组表示如下:
D = ( O , T , E )
把三元组理解为 (实体entity,实体关系relation,实体entity)，把实体看作是结点，把实体关系（包括属性，类别等等）看作是一条边，那么包含了大量三元组的知识库就成为了一个庞大的知识图。

知识库涉及到的两大关键技术是

实体链指(Entity linking) ，即将文档中的实体名字链接到知识库中特定的实体上。它主要涉及自然语言处理领域的两个经典问题实体识别 (Entity Recognition) 与实体消歧 (Entity Disambiguation)，简单地来说，就是要从文档中识别出人名、地名、机构名、电影等命名实体。并且，在不同环境下同一实体名称可能存在歧义，如苹果，我们需要根据上下文环境进行消歧。
关系抽取 (Relation extraction)，即将文档中的实体关系抽取出来，主要涉及到的技术有词性标注 (Part-of-Speech tagging, POS)，语法分析，依存关系树 (dependency tree) 以及构建SVM、最大熵模型等分类器进行关系分类等。

理想的联合学习应该如下图：输入一个句子，通过实体识别和关系抽取联合模型，直接得到有关系的实体三元组。这种可以克服上面流水线方法的缺点，但是可能会有更复杂的结构。参考:https://zhuanlan.zhihu.com/p/31672529

实体提取用哈工大的库pyltp(可以用CTB模型重新做分词模型)，导入官方模型即可，也可以导入自己的

关系提取转换为分类问题，这个我在推理机里已经做了



### QA对自动生成

目前打算先使用基本的NLP和规则来自动生成问题。[PYLTP](https://github.com/HIT-SCIR/pyltp)是哈工大的一个开源中文文本处理python库，我们目前需要用到其中的中文分词和中文词性标注功能。我们目前只对页面进行问题自动生成处理，使用华为云帮助中心每个页面顶部的结构说明（多个标签）为每个页面生成单个问题。

处理方法为：

#### 分标签

这一步可能在spider.py中已经处理了。

#### 筛除对问题生成无用的标签

有些标签对问题生成美元意义，例如第一个永远是“帮助中心”。

另外如“概览”，“FAQ”这样的文字不太可能出现在问题中。

#### 使用PYLTP的分词和词性标注

需要引用PYLTP库和下载模型。

```python
#分词
def segmentor(sentence=''):
    segmentor = Segmentor()  # 初始化实例
    segmentor.load('/Users/zhangqinyuan/Downloads/ltp_data_v3.4.0/cws.model')  # 加载模型
    words = segmentor.segment(sentence)  # 分词
    # 可以转换成List 输出
    words_list = list(words)
    segmentor.release()  # 释放模型
    return words_list

#获取分词后词性
def posttagger(words):
    postagger = Postagger() # 初始化实例
    postagger.load('/Users/zhangqinyuan/Downloads/ltp_data_v3.4.0/pos.model')  # 加载模型
    postags = postagger.postag(words)  # 词性标注
#   for word,tag in zip(words,postags):
#       print (word+'/'+tag)
    postags_list = list(postags)
    postagger.release()  # 释放模型
    return postags_list
```




### 推理机

推理机针对当前问题的条件或已知信息，反复匹配知识库中的规则，获得新的结论，以得到问题求解结果。



       	   	=== 问题分类
       		|           
     问题分析  ---    === 主题提取
    		|
    		=== 关键词提取
   

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





引用
http://www.doc88.com/p-111669478578.html
http://www.doc88.com/p-1465284404817.html

jieba库
    开发者可以指定自己自定义的词典，以便包含 jieba 词库里没有的词。虽然 jieba 有新词识别能力，但是自行添加新词可以保证更高的正确率
    用法： jieba.load_userdict(file_name) # file_name 为文件类对象或自定义词典的路径
    词典格式和 dict.txt 一样，一个词占一行；每一行分三部分：词语、词频（可省略）、词性（可省略），用空格隔开，顺序不可颠倒。file_name 若为路径或二进制方式打开的文件，则文件必须为 UTF-8 编码。
