# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 15:22:11 2017

@author: tedoreve
"""

"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

from wordcloud import WordCloud
import ass
import codecs 
import jieba

text =''

for i in range(14):
    with codecs.open('../data/ass/'+ str(i+1) +'.ass','r',encoding='utf-16-le') as f:
        doc = ass.parse(f)
        for j in range(len(doc.events)):
            text += doc.events[j].text 
#text = open(path.join(d, '../data/constitution.ass')).read()


  
word_jieba = jieba.cut(text,cut_all=False)  
word_split = ",".join(word_jieba)  

word_list  = word_split.split(',')
trash      = ['be1','','fad','frz','pos','an7']
word_list  = list(filter(lambda a: a not in trash, word_list))
word_split = ",".join(word_list)  

# Generate a word cloud image
wordcloud  = WordCloud(font_path='../data/simsun.ttc',width=1600, height=800).generate(word_split)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")
#plt.savefig('sample.jpg', dpi = 600)

# lower max_font_size
#wordcloud = WordCloud(max_font_size=40).generate(text)
#plt.figure()
#plt.imshow(wordcloud)
#plt.axis("off")
#plt.show()

