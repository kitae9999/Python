import requests
from bs4 import BeautifulSoup

url="https://www.fmkorea.com/football_news"
res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml") #우리가 가져온 html문서를 lxml을 통해서 뷰숩객체로만듬
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) #숲은 우리가 가져온 모든 html문서에대한 정보를 가지고있는데 그 중에서 제일 먼저 발견된 a태그 
# print(soup.a.attrs) # a태그의 속성 정보를 출력
# print(soup.a["href"]) # a태그의 href 속성 "값" 정보를 출력

soup.find("a",)