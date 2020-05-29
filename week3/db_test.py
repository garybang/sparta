from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta 

## 코딩 할 준비 ##
findMovie = db.movies.find_one({'title':'매트릭스'})
findStar = findMovie['star']
db.movies.update_many({'star':findStar}, ({'$set':{'star':0}}))

findZeros = list(db.movies.find({'star':0}))
for findZero in findZeros:
    print(findZero['title'], findZero['star'])
