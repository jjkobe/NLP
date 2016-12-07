import jieba

seg_list = jieba.cut_for_search("鞋子质量很好")
print("Full Mode: " + "/ ".join(seg_list))