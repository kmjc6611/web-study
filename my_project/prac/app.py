from flask import Flask, render_template, jsonify, request  # request : 서버에서 클라이언트에게 request보내는데 그 정보를 꺼낼때 사용

# jsonify : 반대로 서버로 줄 때 json형태로 주기 위해 사용한다.
app = Flask(__name__)


## HTML을 주는 부분
@app.route('/')  # 특정 라우팅으로 들어오는 요청을 받아준다.
def home():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/test', methods=['GET'])
def test_get():
    title_receive = request.args.get(
        'title_give')  # get방식에서 파라메타를 꺼내온다. #도메인에서 key : value 방식으로 가져올 때 'title_give'라고 했으므로
    print(title_receive)  # 똑같이 주소창에 값을 입력 할때도 key에는 'title_give'라고 해야한다.
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})


@app.route('/test', methods=['POST'])
def test_post():
    title_receive = request.form['title_give']  # request.form은 dictionary 형태로 넘어오기 때문에 []로 받는다.
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})  # jsonify 영역은 파이썬 문법을 사용해서 작성한다.


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
