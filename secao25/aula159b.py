import pymongo

con = pymongo.MongoClient()

db = con.cadastrodb

print(db.minhacolecao2.find_one())
