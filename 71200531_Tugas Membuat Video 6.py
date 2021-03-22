#Jarjit diminta untuk membuat program yang dapat menggabungkan 2 sampai 3 
#kalimat menjadi sebuah paragraf.
#===============================================================================
#input : pilih,kalimat,paragraf
#proses : membuat beberapa kalimat menjadi sebuah paragraf
#output : Menampilkan hasil paragraf
print("Pilihan berapa kalimat yang tersedia:")
print("1. 2 Kalimat")
print("2. 3 Kalimat")
pilih = int(input("Masukkan nomor sesuai dengan pilihan yang ada : "))
if pilih == 1:
    kalimat1 = str(input("Masukkan kalimat 1 (Beri tanda '.' pada akhir kalimat): "))
    kalimat2 = str(input("Masukkan kalimat 2 (Beri tanda '.' pada akhir kalimat): "))
    kapital1 = kalimat1.capitalize()
    kapital2 = kalimat2.capitalize()
    paragraf = kapital1 + ' ' + kapital2
    print(paragraf)
elif pilih == 2:
    kal1 = str(input("Masukkan kalimat 1 (Beri tanda '.' pada akhir kalimat): "))
    kal2 = str(input("Masukkan kalimat 2 (Beri tanda '.' pada akhir kalimat): "))
    kal3 = str(input("Masukkan kalimat 3 (Beri tanda '.' pada akhir kalimat): "))
    kap1 = kal1.capitalize()
    kap2 = kal2.capitalize()
    kap3 = kal3.capitalize()
    para = kap1 + ' ' + kap2 + ' ' + kap3
    print(para)
else:
    print("Maaf input yang dituliskan tidak sesuai dengan ketentuan.")
