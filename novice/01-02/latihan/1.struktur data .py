#latihan list
belanja=['aple','jeruk','durian','jambu']
print('aku harus beli',len(belanja),'barang di warung')
print('barangnya ini:', end=' ')
for item in belanja:
    print(item, end=' ')

print('\ndan ditambah beli pepaya')
belanja.append('pepaya')
print(belanja)