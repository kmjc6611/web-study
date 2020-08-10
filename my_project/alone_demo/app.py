from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)  몽고DB랑 연결하기 위해 적은 것

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/memo', methods=['POST'])
def post_article():
    # 1. 클라이언트로부터 데이터를 받기
    url_received = request.form['url_get']
    comment_received = request.form['comment_get']

    # 2. meta tag를 스크래핑하기
    url = url_received  # 사용자에게 받은 url에서 크롤링 하기.

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)

    # 여기에 코딩을 해서 meta tag를 먼저 가져와보겠습니다.

    soup = BeautifulSoup(data.text, 'html.parser')

    if not soup.has_attr('meta[property="og:image"]'):
        return jsonify({'result': 'image_fail'})

    if not soup.has_attr('meta[property="og:title"]'):
        return jsonify({'result': 'title_fail'})

    if not soup.has_attr('meta[property="og:description"]'):
        return jsonify({'result': 'description_fail'})

    og_image = soup.select_one('meta[property="og:image"]')['content']  # 따옴표 규칙을 잘 지킬 것.
    og_title = soup.select_one('meta[property="og:title"]')['content']
    og_description = soup.select_one('meta[property="og:description"]')['content']

    # 3. mongoDB에 데이터 넣기
    doc = {
        'url': url_received,
        'comment': comment_received,
        'image': og_image,
        'title': og_title,
        'description': og_description,
    }

    db.articles.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '저장되었습니다!'})


@app.route('/memo', methods=['GET'])
def read_articles():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기(Read)
    articles_from_db = list(db.articles.find({}, {'_id': False}))  # 첫번째 괄호는 검색 조건, 두번째 괄호는 키값 제외 조건

    # 2. articles라는 키 값으로 articles 정보 보내주기
    return jsonify(
        {'result': 'success', 'msg': '하이하이', 'articles': articles_from_db})  # 지금은 페이지 시작할 때 alert를 꺼 놔서 msg가 뜨지 않는다.


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
