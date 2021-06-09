import modal

# query ="select * from produk"
# a = modal.Connection()
# b = a.select(query)
# print(b[0][0])

query ="select tanggal, nominal from pemasukan"
a = modal.Connection()
b = a.select(query)
graph = []
for row in range(len(b)):
    bulan = int(b[row][0][5:7])
    hari = int(b[row][0][8:10])
    data = [hari, bulan]
    graph.append(data)
print(graph)
# nama = 'KN95'
# jenis = 'Masker'
# query = f"insert into produk (nama_produk, jenis_produk, stok, terjual) values ({nama},{jenis},{'0'},{'0'})"
# print(query)
# nama = 'KN95'
# jenis = 'Masker'
# new_obj = modal.Produk(nama,jenis,'0','0')
# query = f"insert into produk (nama_produk, jenis_produk, stok, terjual) values ({new_obj.getNama()}, {new_obj.getJenis()}, {new_obj.getStok()}, {new_obj.getTerjual()})"
# print(query)


# from datetime import datetime

# now = datetime.now()

# date = now.strftime("%Y/%m/%d")
# print("date:",date )