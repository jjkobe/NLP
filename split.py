import re

f = open(r"C:\Users\I321338\PycharmProjects\Segmentation\test10.txt",'r', encoding='utf-8')

text = f.readline()

while text!="":
    file = re.split("\n|，|。|！|\ " ,text)
    for i in file:
        if i != '':
            print(i)
    text = f.readline()