from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)  몽고DB랑 연결하기 위해 적은 것

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    # 여길 채워나가세요!

    # 1. 클라이언트로부터 데이터를 받기
    name_received = request.form['name_get']
    num_received = request.form['num_get']
    address_received = request.form['address_get']
    phoneNum_received = request.form['phoneNum_get']

    # 2. mongoDB에 데이터 넣기
    doc = {
        'name': name_received,
        'num': num_received,
        'address': address_received,
        'phoneNum': phoneNum_received,
    }

    db.orders.insert_one(doc)

    return jsonify({'result': 'success', 'msg': '주문되었습니다!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    # 여길 채워나가세요!

    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기(Read)
    orders_from_db = list(db.orders.find({}, {'_id': False}))  # 첫번째 괄호는 검색 조건, 두번째 괄호는 키값 제외 조건

    # 2. articles라는 키 값으로 articles 정보 보내주기
    return jsonify(
        {'result': 'success', 'msg': '하이하이', 'orders': orders_from_db})  # 지금은 페이지 시작할 때 alert를 꺼 놔서 msg가 뜨지 않는다.


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
