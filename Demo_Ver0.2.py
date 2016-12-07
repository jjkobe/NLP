from snownlp import SnowNLP
import jieba
import jieba.analyse
import re
jieba.load_userdict("mydict.txt")

###############################
#情感分析，判断筛选出负面评论
###############################

typ = [[],[],[]]
typ[0] = []
for word in open ("C:\\Users\\I321338\\PycharmProjects\\Segmentation\\type1.txt","r",encoding="utf8"):
    typ[0].append(word.strip())
    typ[0].append(' ')
typ[1] = []
for word in open ("C:\\Users\\I321338\\PycharmProjects\\Segmentation\\type2.txt","r",encoding="utf8"):
    typ[1].append(word.strip())
    typ[1].append(' ')
typ[2] = []
for word in open ("C:\\Users\\I321338\\PycharmProjects\\Segmentation\\type3.txt","r",encoding="utf8"):
    typ[2].append(word.strip())
    typ[2].append(' ')

result = [[],[],[],[]]
f = open(r"C:\Users\I321338\PycharmProjects\Segmentation\Demo_Ver0.1_500.txt",'r', encoding='utf-8')
r = open(r"C:\Users\I321338\PycharmProjects\Segmentation\Demo_Ver0.1_Sentiment500.txt", 'w', encoding='utf-8')
result[0] = open(r"C:\Users\I321338\PycharmProjects\Segmentation\Demo_Result_type1.txt", 'w', encoding='utf-8')
result[1] = open(r"C:\Users\I321338\PycharmProjects\Segmentation\Demo_Result_type2.txt", 'w', encoding='utf-8')
result[2] = open(r"C:\Users\I321338\PycharmProjects\Segmentation\Demo_Result_type3.txt", 'w', encoding='utf-8')
result[3] = open(r"C:\Users\I321338\PycharmProjects\Segmentation\Demo_Result_other.txt", 'w', encoding='utf-8')
text = f.readline()
while text!="":
    text_snow = SnowNLP(text)
    score = text_snow.sentiments
    if score < 0.4:
        flag = True
        for index,val in enumerate(typ):
            seg_list = jieba.cut(text, cut_all=False)
            for j in seg_list:
                if (j in val) and (j != ' '):
                    result[index].write(str(score) + ' ' + text)
                    flag = False
                    break
        if flag:
            result[3].write(text)
        #r.write(text)
    text = f.readline()
f.close()
r.close()
result[0].close()
result[1].close()
result[2].close()
result[3].close()
# text = f.readline()
# while text!="":
#     seg_list = jieba.cut(text, cut_all=False)
#     output = " ".join(list(seg_list))
#     print("result: " + "/ ".join(seg_list))
#     r.write(output + '\n')
#     text = f.readline()




##############################
#负评分词
##############################
# f = open(r"C:\Users\I321338\PycharmProjects\Segmentation\Demo_Ver0.1_Sentiment500.txt",'r', encoding='utf-8').read()
# r = open(r"C:\Users\I321338\PycharmProjects\Segmentation\Demo_Ver0.1_Seg500.txt", 'w', encoding='utf-8')
# stopwords = []
# for word in open ("C:\\Users\\I321338\\PycharmProjects\\Segmentation\\stop_words.txt","r",encoding="utf8"):
#     stopwords.append(word.strip())
#     stopwords.append(' ')
# seg_list = jieba.cut(f, cut_all=False)
# final =""
# for word in seg_list:
#     if word not in stopwords:
#         if word == '\n':
#             final += word
#         else:
#             final += word + " "
# output = "".join(list(final))
# r.write(output + '\n')
# r.close()