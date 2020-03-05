# Input dan Output

Akan ada situasi di mana program Anda harus berinteraksi dengan pengguna. Misalnya, Anda ingin mengambil input dari pengguna dan kemudian mencetak beberapa hasil kembali. Kita dapat mencapai ini menggunakan fungsi input() dan fungsi print masing-masing.

Untuk output, kita juga bisa menggunakan berbagai metode kelas str (string). Misalnya, Anda dapat menggunakan metode rjust untuk mendapatkan string yang dibenarkan dengan benar untuk lebar yang ditentukan.

# Pemformatan Output yang Lebih Menarik
ada dua cara untuk menulis nilai: pernyataan ekspresi dan fungsi print(). 
(Cara ketiga menggunakan metode write() dari objek file; file output standar dapat dirujuk sebagai sys.stdout . Lihat Referensi Perpustakaan untuk informasi lebih lanjut tentang ini.
Ada beberapa cara untuk memformat output.
 1. string literal yang diformat , mulailah string dengan f atau F sebelum tanda kutip pembuka atau tanda kutip tiga


```python
>>>  year = 2016
>>>  event = 'Referendum'
>>>  f 'Results of the  {year}   {event} '
'Results of the 2016 Referendum'
```

2. Metode str.format() dari string membutuhkan lebih banyak upaya manual. Anda masih akan menggunakan { dan } untuk menandai di mana variabel akan diganti dan dapat memberikan arahan pemformatan terperinci, tetapi Anda juga harus memberikan informasi yang akan diformat.


```python
>>>  yes_votes = 42_572_654
>>>  no_votes = 43_132_495
>>>  percentage = yes_votes / ( yes_votes + no_votes )
>>>  ' {:-9}  YES votes   {:2.2%} ' . format ( yes_votes , percentage )
' 42572654 YES votes  49.67%'
```

# Cara Mengambil Input dari Keyboard

Cara pakainya: 


```python
nama_varabel = input("Sebuah Teks")
```

Artinya, teks yang kita inputkan dari keyboard akan disimpan ke dalam nama_variabel.

contoh:


```python
# Mengambil input
nama = raw_input("Siapa nama kamu: ")
umur = input("Berapa umur kamu: ")

# Menampilkan output
print "Hello",nama,"umur kamu adalah",umur,"tahun"
```

# sumber


```python
1. https://www.petanikode.com/python-input-output/
2. https://docs.python.org/3/tutorial/inputoutput.html
```
