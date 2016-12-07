import jieba
import jieba.analyse

jieba.analyse.set_stop_words("stop_words.txt")
f = open(r"C:\Users\I321338\PycharmProjects\Segmentation\test1000.txt", 'rb').read()
tags = jieba.analyse.extract_tags(f, topK=10, withWeight=True)
for tag in tags:
    print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))
print('=' * 40)
tags2 = jieba.analyse.textrank(f, topK=10, withWeight=True)
for tag2 in tags2:
    print("tag: %s\t\t weight: %f" % (tag2[0],tag2[1]))