import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/list?titleId=675554"
res=requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# cartoons=soup.find_all("td",attrs={"class":"title"}) #리스트로 저장
# # title = cartoons[0].a.get_text()

# for cartoon in cartoons:
#     print(cartoon.a.get_text()) #제목정보
#     print("https://comic.naver.com"+cartoon.a["href"]) #링크정보
    
# 평점 구하기
total_rates=0
cartoons=soup.find_all("div",attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate=cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print("평균 점수 : ",total_rates/len(cartoons))