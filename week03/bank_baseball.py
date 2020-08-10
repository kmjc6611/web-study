import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select("#regularTeamRecordList_table > tr")
for tr in trs:

    rank = tr.select_one("th > strong").text
    team = tr.select_one("td > div > span").text
    rate = tr.select_one("td> strong").text

    if rank is not None:
        if float(rate) > 0.5:
            print(rank, team)
