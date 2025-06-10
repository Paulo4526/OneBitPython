from pymongo import MongoClient

client = MongoClient()

mydb = client.obcblog
mycol = mydb.posts

old_value = {
    "category": "Automação"
}

new_value = {
    "$set": {"category": "Automações em Python"}
}

mycol.update_one(old_value, new_value)

for x in mycol.find():
    print(f"{x}")