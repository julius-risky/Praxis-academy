#file json
import json

#buka file json
file_json=open('userjson.json')

#load file json dari file yang sudah dibuka
data = json.loads(file_json.read())

#cetak isi data
print (data)