from snownlp import sentiment
from snownlp import seg

sentiment.train('neg.txt', 'pos.txt')
sentiment.save('sentiment.marshal')
# seg.train('data.txt')
# seg.save('seg.marshal')