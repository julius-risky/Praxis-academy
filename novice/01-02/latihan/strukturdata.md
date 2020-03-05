# STRUKTUR DATA

Struktur data pada dasarnya hanya itu - mereka adalah struktur yang dapat menyimpan beberapa data bersama. Dengan kata lain, mereka digunakan untuk menyimpan koleksi data terkait.

Ada empat struktur data bawaan di python list, tuple, dictionary dan set.

# Membuat list


```python
# Membuat List kosong
warna = []

# Membuat list dengan isi 1 item
hobi = ["photography"]

# membuat list dengan isi lebih dari 1
buah = ["jeruk", "apel", "mangga", "duren"]
```

# Menambahkan item list

Menambahkan Item List

Tedapat Tiga metode (method) atau fungsi yang bisa digunakan untuk menambahkan isi atau item ke List:

 1.prepend(item) menambahkan item dari depan;
 2.append(item) menambahkan item dari belakang.
 3.insert(index, item) menambahkan item dari indeks tertentu


```python
#list awal
buah = ["jeruk", "apel", "mangga", "duren"]
```

1.prepend(item)


```python
buah = ["jeruk", "apel", "mangga", "duren"]
buah.prepend("anggur")
```

2.appen(item)


```python
buah = ["jeruk", "apel", "mangga", "duren"]
# Tambahkan manggis
buah.append("manggis")
```

3.insert


```python
buah = ["jeruk", "apel", "mangga", "duren"]
buah.insert(2, "duren")
```

# Mengambil list

setelah kita tahu cara membuat dan menyimpan data di dalam List, mari kita coba mengambil datanya.

List sama seperti array, list juga memiliki nomer indeks untuk mengakses data atau isinya

Nomer indeks list selalu dimulai dari nol (0).
Nomer indeks ini yang kita butuhkan untuk mengambil isi (item) dari list.


```python
# Kita punya list nama-nama buah
buah = ["apel", "anggur", "mangga", "jeruk"]

# Misanya kita ingin mengambil mangga
# Maka indeknya adalah 2
print buah[2]
```

# Mengganti nilai list


```python
# list mula-mula
buah = ["jeruk", "apel", "mangga", "duren"]
# mengubah nilai index ke-2
buah[2] = "kelapa"
```

# fungsi lain list


```python
list.extend(iterable)
#Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.remove(x)
#Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

list.pop([i])
#Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

list.clear()
#Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]])
#Return zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.
#The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)
#Return the number of times x appears in the list.

list.sort(key=None, reverse=False)
#Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
#Reverse the elements of the list in place.

list.copy()
#Return a shallow copy of the list. Equivalent to a[:]
```

# Tuple

tuple digunakan untuk menyatukan banyak objek. Anggap mereka mirip dengan daftar, tetapi tanpa fungsionalitas luas yang diberikan kelas daftar kepada Anda. Salah satu fitur utama dari tuple adalah mereka tidak dapat diubah seperti string yaitu Anda tidak dapat memodifikasi tupel.

Tuples didefinisikan dengan menentukan item yang dipisahkan oleh koma dalam sepasang kurung opsional.

Tuples biasanya digunakan dalam kasus-kasus di mana pernyataan atau fungsi yang ditentukan pengguna dapat dengan aman mengasumsikan bahwa pengumpulan nilai (yaitu tupel nilai yang digunakan) tidak akan berubah.

contoh:


```python
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo    # parentheses not required but are a good idea
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
      len(new_zoo)-1+len(new_zoo[2]))
```

output


```python
Number of animals in the zoo is 3
Number of cages in the new zoo is 3
All animals in new zoo are ('monkey', 'camel', ('python', 'elephant', 'penguin'))
Animals brought from old zoo are ('python', 'elephant', 'penguin')
Last animal brought from old zoo is penguin
Number of animals in the new zoo is 5
```

# Sets

Python juga menyertakan tipe data untuk set. Set adalah koleksi yang tidak diurut tanpa elemen duplikat. Penggunaan dasar meliputi pengujian keanggotaan dan menghilangkan entri duplikat. Atur objek juga mendukung operasi matematika seperti penyatuan, persimpangan, perbedaan, dan perbedaan simetris.

Kurung kurawal atau fungsi set () dapat digunakan untuk membuat set. Catatan: untuk membuat set kosong Anda harus menggunakan set (), bukan {}; yang terakhir membuat kamus kosong, struktur data yang kita bahas di bagian selanjutnya.


```python
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```

# Dictionaries

Tipe data lain yang berguna yang dibangun ke dalam Python adalah kamus (lihat Tipe Pemetaan - dict). Kamus kadang-kadang ditemukan dalam bahasa lain sebagai "memori asosiatif" atau "array asosiatif". Tidak seperti urutan, yang diindeks oleh sejumlah angka, kamus diindeks oleh kunci, yang bisa berupa tipe apa pun yang tidak berubah; string dan angka selalu bisa menjadi kunci. Tuples dapat digunakan sebagai kunci jika hanya berisi string, angka, atau tupel; jika sebuah tuple berisi objek yang bisa berubah baik secara langsung atau tidak langsung, itu tidak dapat digunakan sebagai kunci. Anda tidak dapat menggunakan daftar sebagai kunci, karena daftar dapat dimodifikasi di tempat menggunakan penugasan indeks, penugasan slice, atau metode seperti menambahkan () dan memperluas ().

Yang terbaik adalah memikirkan kamus sebagai satu set kunci: pasangan nilai, dengan persyaratan bahwa kunci itu unik (dalam satu kamus). Sepasang kawat gigi membuat kamus kosong: {}. Menempatkan daftar kunci yang dipisah koma: pasangan nilai dalam kurung menambah kunci awal: pasangan nilai ke kamus; ini juga cara kamus ditulis pada output.

Operasi utama pada kamus adalah menyimpan nilai dengan beberapa kunci dan mengekstraksi nilai yang diberikan kunci. Dimungkinkan juga untuk menghapus kunci: pasangan nilai dengan del. Jika Anda menyimpan menggunakan kunci yang sudah digunakan, nilai lama yang terkait dengan kunci itu dilupakan. Merupakan kesalahan untuk mengekstraksi nilai menggunakan kunci yang tidak ada.

Melakukan daftar (d) pada kamus mengembalikan daftar semua kunci yang digunakan dalam kamus, dalam urutan penyisipan (jika Anda ingin diurutkan, gunakan saja diurutkan (d) sebagai gantinya). Untuk memeriksa apakah satu kunci ada di kamus, gunakan kata kunci dalam.



```python
>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```

# sumber

1. https://www.petanikode.com/python-list/
2. https://docs.python.org/3/tutorial/datastructures.html
3. https://python.swaroopch.com/data_structures.html
4. https://www.datacamp.com/community/tutorials/data-structures-python
5. https://docs.python.org/3/tutorial/datastructures.html#dictionaries
