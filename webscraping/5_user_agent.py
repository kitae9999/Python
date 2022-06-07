import requests
url="http://nadocoding.tistory.com"
headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.57 Whale/3.14.133.23 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()


 
with open("nadocoding.html","w",encoding="utf-8") as f:
    f.write(res.text)