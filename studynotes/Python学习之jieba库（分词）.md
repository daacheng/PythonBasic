# 常用功能
参考：http://blog.csdn.net/qq_27231343/article/details/51898940
## 一、分词
支持三种分词模式：</br>
*  全模式:把句子中所有的可以成词的词语都扫描出来, 速度非常快，但是不能解决歧义.
*  精确模式：试图将句子最精确的分开，适合文本分析。
*  搜索引擎模式：在精确模式的基础上，对长词再次切分。粒度比较细，适用于搜索引擎分词。
### 1.1、jieba.cut方法
方法接受三个输入参数: 需要分词的字符串；cut_all 参数用来控制是否采用全模式；HMM 参数用来控制是否使用 HMM 模型。**返回一个生成器generator**
### 1.2、jieba.cut_for_search方法（搜索引擎模式）
方法接受两个参数：需要分词的字符串；是否使用 HMM 模型。**返回一个生成器generator**
### 1.3、jieba.lcut方法、jieba.lcut_for_search方法
这两个方法与上面两个方法用法一样，不同的是lcut返回的是list结果。

    import jieba
    seg_list = jieba.lcut("我来到北京清华大学",cut_all=True)
    print(seg_list)  # 全模式

    words=jieba.lcut('我来到北京清华大学')#精准模式，默认cut_all=False
    print(words)

    print(jieba.lcut_for_search('我来到北京清华大学'))#搜索引擎模式分词
    ['我', '来到', '北京', '清华', '清华大学', '华大', '大学']
    ['我', '来到', '北京', '清华大学']
    ['我', '来到', '北京', '清华', '华大', '大学', '清华大学']

## 二、添加自定义词典
*  开发者可以指定自己自定义的词典，以便包含 jieba 词库里没有的词。虽然 jieba 有新词识别能力，但是自行添加新词可以保证更高的正确率。
*  jieba.load_userdict(file_name),其中参数为自定义的词典的文件路径
*  jieba.suggest_freq(('武汉娃哈哈'),True) #可调节单个词语的词频，使其能（或不能）被分出来。

        jieba.load_userdict('worddict.txt')
        str='武汉娃哈哈信息系统有限公司信息大厦卢志诚实'
        #jieba.suggest_freq(('武汉娃哈哈'),True) #可调节单个词语的词频，使其能（或不能）被分出来。['武汉娃哈哈', '信息系统', '有限公司', '信息大厦', '卢志', '诚实']
        w=jieba.lcut(str)
        print(w)  #['武汉', '娃哈哈', '信息系统', '有限公司', '信息大厦', '卢志', '诚实']
    
