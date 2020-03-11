# membuat data base

membuat data base mahasiswa dengan cara:


```python
create database mahasiswa
```

selanjutnya masuk ke database mahasiswa lalu membuat tabel mahasiswa


```python
#masuk kedalam database
use mahasiswa

#membuat tabel mahasiswa dan menambahkan column nama, nim dan kelas
create tabel mahasiswa (nama VARCHAR(50),Nim INT,kelas text );
```

setelah itu mengecek isi tabel dan sudah terbuat atau belum dengan:


```python
select * from mahasiswa
```


```python
#output
Empty set (0.00 sec)

#tabel masih kosong
```

selanjutnya memasukkan nilai kedalam table:


```python
insert into mahasiswa
    -> (nama,Nim, kelas) values
    -> ("yulius riski",161414099,'C');

#output
Query OK, 3 row affected (0.08 sec)
```


```python
#cek isi table 
select * from mahasiswa

#output
+--------------+-----------+-------+
| Nama         | Nim       | kelas |
+--------------+-----------+-------+
| yulius riski | 161414099 | c     |
+--------------+-----------+-------+
1 row in set (0.00 sec)
```
