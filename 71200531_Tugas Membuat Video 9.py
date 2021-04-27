#Suti diminta untuk membuat sebuah program yang dapat mengetahui nilai dibawah
#KKM dari mahasiswa yang ditentukan. Mahasiswa yang ada adalah 4 orang
#==============================================================================
#input : nama, nilai, jumlah_mahasiswa, KKM
#proses : membuat dictionary nama dan siswa lalu membandingkan dengan KKM
#output : menampilkan nilai yang dibawah KKM

mahasiswa = int(input('Jumlah mahasiswa :'))
kamus = dict()
biji = 0
for i in range (mahasiswa):
    print('================')
    nama = input('Nama :')
    nilai = int(input('Nilai :'))
    kamus[nama] = nilai
    biji += nilai
print('================')
KKM = int(input("KKM yang ditentukan : "))
print('mahasiswa yang mempunyai nilai dibawah KKM :')
for bawah in kamus:
    if kamus[bawah] < KKM:
        print(bawah,':',kamus[bawah])
