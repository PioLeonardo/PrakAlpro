#supri diminta untuk membuat program yang bisa mencari harga terkini jika harga
#jual yang lama akan di diskon. Barang tersebut adalah :
#         Harga awal        |          Diskon
#       Rp1.000.000         |            25
#       Rp945.000           |            30
#       Rp856.000           |            50
#===============================================================================
#input : harga awal, diskon, harga sekarang
#proses : harga sekarang = harga awal - ((harga awal * diskon)/100)
#output : harga sekarang
#===============================================================================

harga_sekarang = lambda harga_awal,diskon=0: harga_awal - ((harga_awal * diskon)/100)

awal = int(input("Masukkan harga awal barang : Rp"))
disk = int(input("Diskon (%):"))
print(harga_sekarang(awal,disk))
