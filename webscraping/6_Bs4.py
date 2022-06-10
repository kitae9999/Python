import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/weekday"
res=requests.get(url)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml") #우리가 가져온 html문서를 lxml을 통해서 뷰숩객체로만듬
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) #숲은 우리가 가져온 모든 html문서에대한 정보를 가지고있는데 그 중에서 제일 먼저 발견된 a태그 
# print(soup.a.attrs) # a태그의 속성 정보를 출력
# print(soup.a["href"]) # a태그의 href 속성 "값" 정보를 출력

# print(soup.find("a",attrs={"class":"Nbtn_upload"}))  #soup객체내에서 "a"에 해당하는 첫번째 엘리먼트 가져옴
# print(soup.find(attrs={"class":"Nbtn_upload"})) 
# print(soup.find("li",attrs={"class":"rank01"})) 
# rank1=soup.find("li",attrs={"class":"rank01"})
# print(rank1.a.get_text())
# print(rank1.next_sibling)
# print(rank1.next_sibling.next_sibling)
# rank2=rank1.next_sibling.next_sibling
# rank3=rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2=rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

# print(rank1.parent)
# rank1.find_next_sibling("li")

# print(rank1.find_next_siblings("li"))

webtoon=soup.find("a",text="나 혼자 만렙 뉴비")
print(webtoon)