from snownlp import SnowNLP
import jieba
import jieba.analyse
import re
jieba.load_userdict("mydict.txt")


f = open(r"C:\Users\I321338\PycharmProjects\Segmentation\test500.txt",'r', encoding='utf-8')
r = open(r"C:\Users\I321338\PycharmProjects\Segmentation\sentiment_test500.txt", 'w', encoding='utf-8')

text = f.readline()
while text!="":
    ###############################
    #如果要把句子根据标点符号分开再来判断，把下面三句话解开注释
    #还要把Snownlp(text)的text改成i，r.write(text)的text改成i
    ###############################

    # file = re.split("\n|，|。|！|\ " ,text)
    # for i in file:
    #      if i != '':
            text_snow = SnowNLP(text)
            score = text_snow.sentiments
            if score < 0.4:
                r.write(text)
                #r.write('/ ' .join(text_snow.words))  #输出分词
                r.write(str(score))
                r.write('\n')
            ############################
            #如果要把句子根据标点符号分开再来判断，把下面这句话和for对齐
            ########################
            text = f.readline()

