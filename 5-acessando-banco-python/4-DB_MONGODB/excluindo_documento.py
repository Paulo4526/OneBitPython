from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

myquery = {"title": "Fast API"}

x = mycol.delete_one(myquery)

print(f"{x.deleted_count} documentos excluídos!")