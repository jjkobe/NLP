import jieba
import jieba.analyse
import jieba.posseg
jieba.load_userdict("mydict.txt")
#####################################
#整个txt一起读进来
#####################################
f = open(r"C:\Users\I321338\PycharmProjects\Segmentation\test10.txt",'r', encoding='utf-8').read()
r = open(r"C:\Users\I321338\PycharmProjects\Segmentation\result_test101.txt", 'w', encoding='utf-8')

stopwords = []
for word in open ("C:\\Users\\I321338\\PycharmProjects\\Segmentation\\stop_words.txt","r",encoding="utf8"):
    stopwords.append(word.strip())
    stopwords.append(' ')
seg_list = jieba.cut(f,cut_all=False)
final =""
for word in seg_list:
    if word not in stopwords:
        if word == '\n':
            final += word
        else:
            final += word + " "
#print(final)
output = "".join(list(final))
# print("result: " + "/ ".join(segs))
r.write(output + '\n')
r.close()

######################################
#一行一行读txt
######################################
# text = f.readline()
# while text!="":
#     seg_list = jieba.cut(text, cut_all=False)
#     output = " ".join(list(seg_list))
#     print("result: " + "/ ".join(seg_list))
#     r.write(output + '\n')
#     text = f.readline()


