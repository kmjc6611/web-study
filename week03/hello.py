import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select("#old_content > table > tbody > tr")
for tr in trs:

    title = tr.select_one("td.title > div > a")
    rank = tr.select_one("td > img")
    point = tr.select_one("td.point")

    if title is not None:
        print("영화 제목 :", "'"+title.text+"'", "|", "순위 :", rank['alt']+"등", "|", "평점 :", point.text+"점")
