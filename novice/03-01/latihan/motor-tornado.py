from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.tokobuku
buku = db.buku

post = buku.find_one({"judul": "tutorial python"})
print(post)