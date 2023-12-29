import pymongo

con = pymongo.MongoClient()

db = con.cadastrodb

colecao = db["minhacolecao2"]

n = colecao.count()

print(n)