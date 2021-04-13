#Budi diminta untuk membuat program yang dapat mencari nilai 5 mahasiswa yang
#ada dalam file yang sudah diberikan kepada Budi
#==============================================================================
#input = file mahasiswa, nama mahasiswa
#proses = membuat keluaran menghasilkan nilai nama mahasiswa yang diinput user
#output = Nilai mahasiswa
#==============================================================================
buka = open("Nilai mahasiswa.txt","r")
baca = str(buka.read())
buka.close()
lst = baca.split('\n')
nama = str(input("Nama Mahasiswa(Huruf depan memakai huruf kapital) : "))
if nama == 'Pio':
    print("Nilai mahasiswa adalah ",lst[0])
elif nama == 'Budi':
    print("Nilai mahasiswa adalah ",lst[1])
elif nama == 'Sanjaya':
    print("Nilai mahasiswa adalah ",lst[2])
elif nama == 'Supri':
    print("Nilai mahasiswa adalah ",lst[3])
elif nama == 'Ujang':
    print("Nilai mahasiswa adalah ",lst[4])
else:
    print("Anda salah input nama. Silahkan dicoba kembali.")
