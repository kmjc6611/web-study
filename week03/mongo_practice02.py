from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

user = db.movies.find_one({'title': '월-E'})
# print(user['star'])           //1번 문제

star = user['star']

# users = db.movies.find({'star': {'$eq': star}})           //2번 문제
# for temp in users:
#     print(temp['title'])
print(star)
db.movies.update_many({'star': {'$eq': star}}, {'$set': {'star': '1'}})
# db.movies.update_many({'star': star}, {'$set': {'star': '1'}})            //똑같음
