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

# 텍스트 분석
# https://wikidocs.net/22650
from konlpy.tag import Okt
okt = Okt()

def build_bag_of_words(document):
  # 온점 제거 및 형태소 분석
  document = document.replace('.', '')
  tokenized_document = okt.morphs(document)

  word_to_index = {}
  bow = []

  for word in tokenized_document:  
    if word not in word_to_index.keys():
      word_to_index[word] = len(word_to_index)  
      # BoW에 전부 기본값 1을 넣는다.
      bow.insert(len(word_to_index) - 1, 1)
    else:
      # 재등장하는 단어의 인덱스
      index = word_to_index.get(word)
      # 재등장한 단어는 해당하는 인덱스의 위치에 1을 더한다.
      bow[index] = bow[index] + 1

  return word_to_index, bow






#okt.morphs( projects["title"] )

nrows = len( projects )

for i in range(0, nrows):
    vocab, bow = build_bag_of_words(titles[i])



