from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# insert / find / update / delete

# 1. 매트릭스 평점 가져오기
movie = db.movies.find_one({'title': '매트릭스'})
target_star = movie['star']
print(target_star)

# 2. 매트릭스 평점과 같은 평점의 영화제목 가져오기
target_movies = list(db.movies.find({'star': target_star}, {'_id':False}))
for target in target_movies:
    print(target['title'])

# 3. 매트릭스 영화 평점 0으로 만들기
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':0}})

# 저장 - 예시
#doc = {'name':'bobby','age':21}
#db.users.insert_one(doc)

# 한 개 찾기 - 예시
#user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
#same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
#db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
#db.users.delete_one({'name':'bobby'})