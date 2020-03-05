# modul

Modul adalah file yang berisi definisi dan pernyataan Python. Nama file adalah nama modul dengan akhiran .py ditambahkan. Dalam sebuah modul, nama modul (sebagai string) tersedia sebagai nilai variabel global __name__ . Misalnya, gunakan editor teks favorit Anda untuk membuat file bernama fibo.py di direktori saat ini dengan konten berikut


```python
# Fibonacci numbers module

def fib ( n ):    # write Fibonacci series up to n
    a , b = 0 , 1
    while a < n :
        print ( a , end = ' ' )
        a , b = b , a + b
    print ()

def fib2 ( n ):   # return Fibonacci series up to n
    result = []
    a , b = 0 , 1
    while a < n :
        result . append ( a )
        a , b = b , a + b
    return result
```

Sekarang masukkan interpreter Python dan impor modul ini dengan perintah berikut:


```python
import fibo
```

# sumber 

1. https://python.swaroopch.com/modules.html
2. https://docs.python.org/3/tutorial/modules.html
