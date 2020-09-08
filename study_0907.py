#%%

from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer

import konlpy 
from konlpy.tag import Okt 
okt=Okt()


words = []
words.append('영희 철수 감사합니다 사기 😂 무료 최고 ㅎㅎ ') # 댓글에 추출된 형태소 혹은 명사
words.append('최고 축하 감사하다 무료') # 긍정 단어 목록
words.append('중단 아 실망 사기 분노') # 부정 단어 목록

    
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




