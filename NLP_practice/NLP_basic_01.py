# Excel 읽기를 위해 xlrd(xls)와 openpyxl 패키지 인스톨
import pandas as pd
import os

# print( os.getcwd() )
os.chdir( os.path.dirname(os.path.realpath(__file__) ) )

file_name = "prism_2023_01.xlsx"
df1 = pd.read_excel(file_name, dtype=str)
df1 = df1[ ["발주기관명", "사업명"]]
print( df1 )

file_name = "public_offerings_2023.xlsx"
df2 = pd.read_excel(file_name, dtype=str)
df2 = df2[ ["공모기관", "사업명"]]
print( df1 )

# 열이름 변경
df1 = df1.rename( columns={"발주기관명": "agency", "사업명": "title"})
df2 = df2.rename( columns={"공모기관": "agency", "사업명": "title"})

# 두 데이터프레임 합치기 : pd.concat()
projects = pd.concat( [df1, df2] )
projects.info()
# print( projects["title"].astype("string").info() )

titles = projects["title"].tolist()
agenciess = projects["agency"].tolist()

# 헌법말뭉치 kolaw 국회법안말뭉치 kobill
from konlpy.corpus import kolaw
# print( kolaw.fileids() )

# print( titles )


# KoNLPy
from konlpy.tag import Okt
okt = Okt()

# https://jeonjoon.tistory.com/32
titles_one = " ".join(titles)
raw_pos_tagged = okt.pos(titles_one, norm=True, stem=True) # POS Tagging
# print(raw_pos_tagged)

del_list = ["를", "이", "은", "는", "있다", "하다", "에"]
word_cleaned = []

# 불용어 처리 및 한글자 이상
for word in raw_pos_tagged:
    if not word[1] in ["Josa", "Eomi", "Punctuation", "Number", "Foreign"]:
        if (len(word[0]) != 1) & (word[0] not in del_list):
            word_cleaned.append(word[0])

# print( word_cleaned )
            
from collections import Counter
            
result = Counter( word_cleaned )
word_dic = dict( result )

# 정렬 
# word_dic.imtes( )를 통해 딕셔너리의 key, value쌍을 튜플로 받습니다.
# 이 튜플에서 lambda함수에 output값으로 x[1]을 설정하여 단어의 개수를 key파라미터의 값으로 합니다.
sorted_word_dic = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
print(sorted_word_dic)

import nltk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 그래프에 한글 폰트 설정
font_name = matplotlib.font_manager.FontProperties(fname="/Users/yoonani/Library/Fonts/KoPubWorld Dotum Light.ttf").get_name() # NanumGothic.otf
matplotlib.rc('font', family=font_name)

word_counted = nltk.Text(word_cleaned)
plt.figure(figsize=(15,7))
word_counted.plot(50)




# # 워드 카운팅
# # https://datascienceschool.net/03%20machine%20learning/03.01.02%20KoNLPy%20%ED%95%9C%EA%B5%AD%EC%96%B4%20%EC%B2%98%EB%A6%AC%20%ED%8C%A8%ED%82%A4%EC%A7%80.html
# from nltk import Text

# titles_word = Text( okt.nouns(titles_one) )
# #print( titles_word.vocab() )

# # titles_word.plot(30)
# # plt.show()

# # 동국대 문서 http://bigdata.dongguk.ac.kr/lectures/TextMining/_book/%ED%85%8D%EC%8A%A4%ED%8A%B8-%EC%9E%90%EB%A3%8C%EC%9D%98-%ED%91%9C%ED%98%84-text-representation.html#%EB%8B%A8%EC%96%B4%EC%9D%98-%ED%91%9C%ED%98%84-%EB%B0%A9%EB%B2%95


# # =======================================================    
# # 형태소(POS)가 명사,동사,알파벳,숫자에 해당되는 단어 추출
# # 정규화(normalization) 어간추출(stemming) 처리
# # =======================================================    
# def tokenizer(raw_texts, pos=["Noun","Alpha","Verb","Number"], stopword=[]):
#     p = okt.pos(raw_texts, 
#             norm=True,   # 정규화(normalization)
#             stem=True    # 어간추출(stemming)
#             )
#     o = [word for word, tag in p if len(word) > 1 and tag in pos and word not in stopword]
#     return(o)

# oo = okt.pos( titles[0], norm=True, stem=True)
# # print( oo )
# # print( tokenizer(titles[0]) )

# # TF-IDF 기반 DTM
# from sklearn.feature_extraction.text import TfidfVectorizer

# vectorize = TfidfVectorizer(
#     tokenizer=tokenizer, # 문장에 대한 tokenizer (위에 정의한 함수 이용)
#     min_df=1,            # 단어가 출현하는 최소 문서의 개수
#     sublinear_tf=True    # tf값에 1+log(tf)를 적용하여 tf값이 무한정 커지는 것을 막음
# )

# X = vectorize.fit_transform(titles)
# X.toarray() 
# # print( X )


# # cosine similarity
# from sklearn.metrics.pairwise import cosine_similarity

# # print( cosine_similarity(X[0], X[1]) )

