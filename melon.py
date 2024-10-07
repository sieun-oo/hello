import requests
from bs4 import BeautifulSoup

# 웹에 접속
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36"}
r = requests.get("https://www.melon.com/",headers=header)
print(r) # 접속이 잘됐는지 확인

# html 정보 가지고오기
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup) # 가져온 html 데이터 출력

# #const > div.chart > div > ul > li.on.nth1 > div > ul > li:nth-child(1) > div.rank_cntt > div.rank_info > p > a
fot i in range(1,11):
    title = soup.select_one(f'#const > div.chart > div > ul > li.on.nth1 > div > ul > li:nth-child(i) > div.rank_cntt > div.rank_info > p > a')
    printf(f'{i}위 {title.text}')

# 노래 제목
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a
title = soup.select('div.ellipsis.rank01 > span > a')
for t in title:
    print(t.text)
# 가수 이름
#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a
artist = soup.select('div.ellipsis.rank02 > span > a')
for t in artist:
    print(t.text)
# 1위 - 50위까지 출력해보기