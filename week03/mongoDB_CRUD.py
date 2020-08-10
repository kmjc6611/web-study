from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

# Create(생성)
user = {'name': '론', 'age': 40}
db.users.insert_one(user)

# Read(조회) - 한 개 값만
user = db.users.find_one({'name': '론'})

# Read(조회) - 여러 값 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age': 40}, {'_id': False}))

# Update(업데이트)
db.users.update_one({'name': '덤블도어'}, {'$set': {'age': 116}})

# Delete(삭제)
db.users.delete_one({'name': '론'})