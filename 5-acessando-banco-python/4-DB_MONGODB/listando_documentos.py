from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

result1 = mycol.find_one()
print(f"Valor sem iteração:\n{result1}\n")

result = mycol.find()
print("Valor com iteração:")
for posts in result:
    print(f"{posts}")