from snownlp import SnowNLP
import jieba
import jieba.analyse
import re
jieba.load_userdict("mydict.txt")

###############################
#情感分析，判断筛选出负面评论
###############################
f = open(r"C:\Users\I321338\PycharmProjects\Segmentation\Demo_Ver0.1_500.txt",'r', encoding='utf-8')
r = open(r"C:\Users\I321338\PycharmProjects\Segmentation\Demo_Ver0.1_Sentiment500.txt", 'w', encoding='utf-8')
text = f.readline()
while text!="":
    text_snow = SnowNLP(text)
    score = text_snow.sentiments
    if score < 0.4:
       r.write(text)
    text = f.readline()
f.close()
r.close()

##############################
#负评分词
##############################
f = open(r"C:\Users\I321338\PycharmProjects\Segmentation\Demo_Ver0.1_Sentiment500.txt",'r', encoding='utf-8').read()
r = open(r"C:\Users\I321338\PycharmProjects\Segmentation\Demo_Ver0.1_Seg500.txt", 'w', encoding='utf-8')
stopwords = []
for word in open ("C:\\Users\\I321338\\PycharmProjects\\Segmentation\\stop_words.txt","r",encoding="utf8"):
    stopwords.append(word.strip())
    stopwords.append(' ')
seg_list = jieba.cut(f, cut_all=False)
final =""
for word in seg_list:
    if word not in stopwords:
        if word == '\n':
            final += word
        else:
            final += word + " "
output = "".join(list(final))
r.write(output + '\n')
r.close()

###########################
#tf-idf和textrank算法统计
###########################
f = open(r"C:\Users\I321338\PycharmProjects\Segmentation\Demo_Ver0.1_Seg500.txt", 'rb').read()
print('=' * 40)
print('tf-idf算法结果如下：')
tags = jieba.analyse.extract_tags(f, topK=10, withWeight=True)
for tag in tags:
    print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))
print('=' * 40)
print('textrank算法结果如下：')
tags2 = jieba.analyse.textrank(f, topK=10, withWeight=True)
for tag2 in tags2:
    print("tag: %s\t\t weight: %f" % (tag2[0],tag2[1]))
