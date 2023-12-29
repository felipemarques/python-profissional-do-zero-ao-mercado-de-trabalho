import pymongo

con = pymongo.MongoClient()

db = con.cadastrodb

for doc in db.minhacolecao2.find():
    print(doc)