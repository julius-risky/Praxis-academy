# Errors and Exceptions.

Sampai sekarang pesan kesalahan belum lebih dari yang disebutkan, tetapi jika Anda telah mencoba contohnya, Anda mungkin telah melihat beberapa. Ada (setidaknya) dua jenis kesalahan yang dapat dibedakan: kesalahan sintaksis dan pengecualian .

# 1.Kesalahan Sintaksis

Kesalahan sintaksis, juga dikenal sebagai kesalahan parsing, mungkin jenis keluhan paling umum yang Anda dapatkan saat Anda masih belajar Python:


```python
 >>>  while True print ( 'Hello world' )
  File "<stdin>" , line 1
    while True print ( 'Hello world' )
                   ^
SyntaxError : invalid syntax
```

# 2.exception

Bahkan jika suatu pernyataan atau ungkapan secara sintaksis benar, itu dapat menyebabkan kesalahan ketika suatu usaha dilakukan untuk mengeksekusinya. Kesalahan yang terdeteksi selama eksekusi disebut pengecualian dan tidak berakibat fatal: Anda akan segera belajar cara menanganinya dalam program Python. Namun, sebagian besar pengecualian tidak ditangani oleh program, dan menghasilkan pesan kesalahan seperti yang ditunjukkan di sini:


```python
 >>>  10 * ( 1 / 0 )
Traceback (most recent call last):
  File "<stdin>" , line 1 , in <module>
ZeroDivisionError : division by zero
>>>  4 + spam * 3
Traceback (most recent call last):
  File "<stdin>" , line 1 , in <module>
NameError : name 'spam' is not defined
>>>  '2' + 2
Traceback (most recent call last):
  File "<stdin>" , line 1 , in <module>
TypeError : Can't convert 'int' object to str implicitly
```

# 3. menangani exceptions

perhatikan bahwa gangguan yang dibuat pengguna ditandai dengan meningkatkan exceptions KeyboardInterrupt 


```python
>>>  while True :
...     try :
...         x = int ( input ( "Please enter a number: " ))
...         break
...     except ValueError :
...         print ( "Oops!  That was no valid number.  Try again..." )
...
```

Pernyataan try berfungsi sebagai berikut.

    1.Pertama, klausa coba (pernyataan) antara try dan except kata kunci) dieksekusi.

    2.Jika tidak ada pengecualian terjadi, kecuali klausa dilewati dan eksekusi pernyataan try selesai.

    3.Jika pengecualian terjadi selama eksekusi klausa coba, sisa klausa dilewati. Kemudian jika jenisnya cocok dengan pengecualian yang dinamai dengan kata kunci except , klausa kecuali dijalankan, dan kemudian eksekusi berlanjut setelah pernyataan try .

    4.Jika pengecualian terjadi yang tidak cocok dengan pengecualian yang disebutkan dalam klausa kecuali, itu diteruskan ke pernyataan try luar; jika tidak ada pawang yang ditemukan, itu adalah pengecualian yang tidak tertangani dan eksekusi berhenti dengan pesan seperti yang ditunjukkan di atas. 

# sumber

1.https://docs.python.org/3/tutorial/inputoutput.html
