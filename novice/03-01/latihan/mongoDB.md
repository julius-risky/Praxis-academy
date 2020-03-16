# Menggunakan MongoDB


# cara intall mongoDB windows

pertama download aplikasi mongoDB pada web:https://www.mongodb.com/download-center/community 
cari os windows dan version 4.2.3(bebas bisa yang mana saja), selanjutnya pilih package msi atau zip.

setelah di download lalu install : https://medium.com/@LondonAppBrewery/how-to-download-install-mongodb-on-windows-4ee4b3493514 dgn mengikuti step link tersebut.

# Start mongoDB di cmd

1. masuk kedalam directori mongo untuk pc saya C:\Program Files\MongoDB\Server\4.2\bin 
2. selanjutnya ketikkan mongo untuk menjalankan mongodb C:\Program Files\MongoDB\Server\4.2\bin>mongo
3. maka mongodb berhasil di jalankan. untuk melihat apakah mongodb sudah berjalan ketikkan db maka akan muncul test, dan shows db untuk belihat database

# membuat database

1. Silahkan ketik perintah ```use tokobuku``` untuk membuat dan menggunakan database tokobuku.
2. lalu untuk mengecek tuliskan ```db tokobuku```
3. untuk memasukkan dengan code:


```python
db.buku.insert({   #colection
    judul:"Buku gambar",
    pengarang:"juki",
    harga:40000,
    field:value, #format data
    field1:value1,
    .
    .
})
```

bisa juga dengan


```python
1. db.collection.insertOne() #untuk memasukkan satu
    
db.collection.insertOne(
   <document>,
   {
      writeConcern: <document>
   }
)


2. db.collection.insertMany() #memsukkan langsung banyak data

db.collection.insertMany(
   [ <document 1> , <document 2>, ... ],
   {
      writeConcern: <document>,
      ordered: <boolean>
   }
)
```

menampilkan isi data
```db.<koleksi>.find()``` 


```python
#dalam contoh diatas dituliskan
db.buku.find()
#untuk bentuk yang lebih rapi dapat ditulis dengan:
db.buku.find().pretty()
#mencari data 
db.buku.find({ harga: 40000 })
```

mengecek jumlah data
```db.<koleksi>.count()```


```python
db.buku.count()
```

mengubah data
```db.<koleksi>.update(<query>, <data baru>)```


```python
db.buku.update(
    {
        judul: "Buku gambar"
    },
    {
        judul:"Buku Gambar",
        pengarang:"juki",
        harga:50000,
    }
)
```

menghapus data
```db.<koleksi>.remove(<query>)```


```python
db.buku.remove(judul:"Buku Gambar")
```

menghapus koleksi
```db.<koleksi>.drop();```
    
menghapus database
```db.dropDatabase();```

# keluar dari mongoDB

pencet ctrl+C

# sumber

1. https://www.petanikode.com/tutorial-dasar-mongodb/
2. https://docs.mongodb.com/manual/crud/
