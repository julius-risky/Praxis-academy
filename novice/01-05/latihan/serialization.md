# Object serialization

# Pickle

pickle digunakan untuk mengimplementasikan protokol biner untuk membuat serial dan menderialisasi struktur objek Python.
    1.pickling adalah  proses di mana hierarki objek Python dikonversi menjadi aliran byte.
    2.unpickling adalah kebalikan dari proses Pickling di mana aliran byte diubah menjadi hierarki objek.

pickle adalah sebuah modul pada standard library python, yang dapat digunakan untuk menyimpan dan membaca data ke dalam /dari sebuah file.

# module interface:

    1.dumps () - Fungsi ini dipanggil untuk mengelompokkan hierarki objek.
    2.Loads () - Fungsi ini dipanggil untuk menghilangkan aliran data serial.

    Untuk kontrol lebih banyak atas serialisasi dan de-serialisasi, masing-masing objek Pickler atau Unpickler dibuat. 

contoh pengunaan fungsi dumps untuk meyimpan data:


```python
    import pickle
    # Nama fike tempat menyimpan data
    file_data = 'namasiswa.data'
    # Data nama siswa
    nama_siswa = ['Diandra', 'Solikin', 'Rommy']
    # Siapkan file untuk ditulis
    f = open(file_data, 'wb')
    # Simpan data nama siswa ke dalam file dengan perintah dump
    pickle.dump(nama_siswa, f)
    f.close() # tutup setelah file digunakan
```

contoh penggunaan fungsi loads untuk membaca data:


```python
    import pickle
    file_siswa = 'namasiswa.data'
    # buka file namasiswa.data
    f = open(file_siswa, 'rb')
    # load data dari file tersebut
    nama_siswa = pickle.load(f)
    f.close()
    print(nama_siswa)
```

# Konstanta yang disediakan oleh modul pickle:

1.pickle.HIGHEST_PROTOCOL
    Ini adalah nilai integer yang mewakili versi protokol tertinggi yang tersedia. Ini dianggap sebagai nilai protokol yang dilewatkan ke fungsi dump (), dumps ().
2.pickle.DEFAULT_PROTOCOL
    Ini adalah nilai integer yang mewakili protokol default yang digunakan untuk pengawetan yang nilainya mungkin kurang dari nilai protokol tertinggi. 

# 1. Cara membuat file json

JSON (JavaScript Object Notation) adalah sebuah format data yang digunakan untuk pertukaran dan penyimpanan data.

struktur data JSON selalu dimulai dengan tanda kurung kurawal { dan ditutup dengan kurung }.

Lalu di dalam kurung kurawal, berisi data yang format key dan value. Jika terdapat lebih dari satu data, maka dipisah dengan tanda koma dan di data terakhir tidak diberikan koma.

contoh:


```python
{
    "name":"julius risky",
    "umur":22,
    "hobi":["Photography","videography","traveling"],
    "email":"julius.risky@gmail.com"
}
```

# Cara parsing file Json ke python

struktur data diatas diberi nama biodata.json


```python
#file json
import json

#buka file json
file_json=open('F:\\Praxis-academy\\novice\\01-05\\kasus\\Biodata.json')

#load file json dari file yang sudah dibuka
data = json.loads(file_json.read())

#cetak isi data
print (data)
```

# membuat file XML

XML (eXtensible Markup Language) adalah sebuah bahasa markup seperti HTML yang didesain untuk menyimpan dan mengantarkan data

 1.Deklarasi: Adalah bagian penting dalam XML, biasanya digunakan untuk menentukan versi XML yang akan digunakan.

    <?xml version="1.0"?>

 2.Elemen: berisi tag-tag yang mendefinisikan sebuah data objek.

 3.Atribut: berisi keterangan tambahan dari objek.
 
contoh :


```python
<?xml version="1.0"?>
<biodata>
    <name>julius riski</name>
    <umur>22</umur>
    <hobi name="traveling"/>
    <hobi name="Membaca Buku"/>
    <hobi name="Nonton Anime"/>
    <email>"julius.riskyGmail.com"</email>
</biodata>
```

# cara parsing XML


```python
import xml.dom.minidom as minidom

def main():
    # gunakan fungsi parse() untuk me-load xml ke memori 
    # dan melakukan parsing
    doc = minidom.parse("F:\\Praxis-academy\\novice\\01-05\\kasus\\biodata.xml")

    # Cetak isi doc dan tag pertamanya
    print (doc.nodeName)
    print (doc.firstChild.tagName)

    name = doc.getElementsByTagName("name")[0].firstChild.data
    umur = doc.getElementsByTagName("umur")[0].firstChild.data
    email = doc.getElementsByTagName("email")[0].firstChild.data
    list_hobi= doc.getElementsByTagName("hobi")
    print ("Nama: {}\numur: {}\nemail: {}\n".format(name, umur, email))

    print ("Memiliki {} hobi:".format(len(list_hobi)))

    for hobi in list_hobi:
        print ("-", hobi.getAttribute("name"))
if __name__ == "__main__":
    main()
```

# sumber


```python
1. https://www.petanikode.com/xml-untuk-pemula/
2. https://www.petanikode.com/json-pemula/
3. https://docs.python.org/3/library/pickle.html
```
