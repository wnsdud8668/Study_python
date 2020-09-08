# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 02:23:50 2020

@author: junyoung
"""


import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import re
import time
from collections import Counter
from wordcloud import WordCloud
from konlpy.tag import Twitter
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import konlpy 
from konlpy.tag import Okt 


#%%

from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer

import konlpy 
from konlpy.tag import Okt 
okt=Okt()

#%%
words = []
words.append('영희 철수 감사합니다 사기 😂 무료 최고 ㅎㅎ ') # 댓글에 추출된 형태소 혹은 명사
words.append('최고 축하 감사하다 무료') # 긍정 단어 목록
words.append('중단 아 실망 사기 분노') # 부정 단어 목록

    
#%%
# 1. 불용어 제거
import re
import pandas as pd
from nltk.tokenize import word_tokenize

# 이모티콘
emoji_pattern = re.compile("["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                u'\U00010000-\U0010ffff'  # not BMP characters
    "]+", flags=re.UNICODE)

# 특수문자, 의성어
han = re.compile(r'[ㄱ-ㅎㅏ-ㅣ!?~,".\n\r#\ufeff\u200d]')

# 이모티콘, 특수문자, 의성어 제거
word_result = []
for i in words:
    tokens = re.sub(emoji_pattern,"",str(i))
    tokens = re.sub(han,"",tokens)
    word_result.append(tokens)



# 불용어 리스트
stop_words = ['아 그 저']

# 불용어 토큰화
for word in stop_words:
    stop_words_token=word_tokenize(word)

# 불용어 제거
token_words=[]
for word in word_result:
    tokens=word_tokenize(str(word))
    words=[]
    for wor in tokens:
        if wor not in stop_words_token:
            words.append(wor)
    token_words.append(words)

print(token_words)

    
#%% 한국어 처리

from konlpy.tag import Okt 
okt=Okt()

okt.morphs('감사합니다')

# morphs = 텍스트를 형태소로 나눈다
# stem = 단어의 어간 추출
okt.morphs('감사합니다',stem=True)
okt.morphs('감사하다 감사합니다 감사',stem=True)

# pos - 텍스트의 품사를 태그
okt.pos('감사합니다 감사해요 감사했습니다')

okt.phrases('감사합니다')


from konlpy.tag import Twitter
twitter=Twitter()

for word in ['했다', '했지만', '하면서도', '했던', '하니까']:
    print(twitter.pos(word))


from konlpy.tag import Komoran

Komoran().pos('했다') # [('하', 'VV'), ('았', 'EP'), ('다', 'EC')]

a=Komoran().pos('감사했습니다 사랑했어요 게임 롯데마트 최고야')

for i in a:
    if i[1]=='NNG' or i[1]=='NNP':
        print(i[0])








#%%
# 부정 단어 리스트
f = open('negative_words_self.txt', 'r',encoding='UTF-8')
lines = f.readlines()
f.close()

negative=[]
for i in lines:
    i=i.replace('\n','')
    negative.append(i)
    
#%%
# 이모티콘 제거
emoji_pattern = re.compile("["
                u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                u'\U00010000-\U0010ffff'  # not BMP characters
    "]+", flags=re.UNICODE)

# 분석에 어긋나는 불용어구 제외 (특수문자, 의성어)
han = re.compile(r'[ㄱ-ㅎㅏ-ㅣ!?~,".\n\r#\ufeff\u200d]')
  

comment_result = []
for i in comm:
    tokens = re.sub(emoji_pattern,"",str(i))
    tokens = re.sub(han,"",tokens)
    comment_result.append(tokens)

# 불용어 제거
words2=[]
for i in words:
    a=[]
    for z in i:
        if z not in stop_words:
            a.append(z)
    words2.append(a)

words2=[]
for i in words:
    a=[]
    for z in i:
        if z not in stop_words:
            a.append(z)
    words2.append(a)

#%% 불용어 제거

# 불용어리스트 로드
f = open('불용어리스트.txt', 'r',encoding='UTF-8')
lines = f.readlines()
f.close()
stop_words=[]
for i in lines:
    stop_words.append(i.replace('\n',''))
print(stop_words)

# 토큰화
words=[]
for i in range(len(df_comment_result)):
    word_tokens=[]
    word_tokens = word_tokenize(str(df_comment_result['comment'].iloc[i]))
    print(word_tokens)
    words.append(word_tokens)

# 불용어 제거
words2=[]
for i in words:
    a=[]
    for z in i:
        if z not in stop_words:
            a.append(z)
    words2.append(a)

#%% 형태소 추출
    

words4=[]
for i in words2:
    c=[]
    for z in i:
        b=okt.morphs(str(z),stem=True)
        c.append(' '.join(b))
    words4.append(' '.join(c).split())

words2=words4
#%% 

#1. comment의 단어가 positive,negative 단어 리스트에 있는지 확인

label=[]    

for i in words2:
    pos=0
    neg=0
    for z in i:
        
        if z in positive:
            pos+=1
        elif z in negative:
            neg+=1
    if pos>neg:
        label.append('1')
    elif pos<neg:
        label.append('-1')
    else:
        label.append('0')

#%%
from sklearn.feature_extraction.text import TfidfVectorizer
#2. 유사도 측정

tfidf_vectorizer=TfidfVectorizer()
words

tfidf_vectorizer = TfidfVectorizer(min_df=1)

label2=[]
for i in words2:
    a=[]
    a.append(' '.join(i))
    a.append(' '.join(positive))
    a.append(' '.join(negative))
    tfidf_matrix_twitter = tfidf_vectorizer.fit_transform(a)
    document_distance = (tfidf_matrix_twitter * tfidf_matrix_twitter.T)
    if document_distance.toarray()[0][1] > document_distance.toarray()[0][2]:
        label2.append('1')
    elif document_distance.toarray()[0][1] < document_distance.toarray()[0][2]:
        label2.append('-1')
    else:
        label2.append('0')

#%%
comment_valid=pd.DataFrame(columns=['comment','단어포함여부','유사도측정'])
comment_valid['comment']=words2
comment_valid['단어포함여부']=label
comment_valid['유사도측정']=label2

comment_valid['단어포함여부'].value_counts().plot(kind='bar')

