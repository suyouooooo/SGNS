# 基于Skip-Gram with Negative Sampling(SGNS)的汉语词向量学习和评估

## 实验说明
本实验所需的全部文件和生成的全部文件均存放在file_dir文件下。

## 实验步骤
### 1 xml2txt.py 将zhwiki.xml转化成zhwiki.txt格式
使用gensim包的WikiCorpus方法将zhwiki*.xml.bz2文件转化为corpus.zhwiki.txt  
使用命令
```
python xml2txt.py input_file output_file
```
### 2 traditional2simplified.py 将zhwiki.txt中的繁体字转化为简体字
将zh_wiki*.xml.bz2 转化为 corpus_zhwiki.txt 后发现，语料中带有大量的繁体字，所以使用opencc库将繁体字转化为简体字  
使用命令  
```
python traditional2simplified.py input_file output_file
```
### 3 segment.py 清洗数据并分词

使用正则表达式去掉一些特殊字符，并使用jieba进行分词

使用命令
```
python segment.py input_file output_file
```
### 4 train.py 训练word2vec模型

使用gensim的word2vec方法进行训练模型，这里提供了一些参数供训练，列出一些重要的参数  

使用命令
```
python train.py input_file out_model out_vector min_count
```

### 5 test.py 测试word2vec模型

这里使用word2vec_model.wv.similarity方法，对pku_sim_test.txt进行测试，进行两个词词向量的余弦距离计算 

使用命令
```
python test.py input_file output_file path_Word2Vec_Model path_Word2Vec_Vec
```