#Badit diminta untuk membuat program yang dapat menilai suatu hasil pekerjaan
#5 mahasiswa apakah nilai tersebut tergolong mampu atau harus belajar kembali
#dengan KKM 70. Nilai mahasiswanya adalah : 1. 56, 2. 96, 3. 67, 4. 75, 5. 83.
#============================================================================
#input: jumlah mahasiswa, nilai
#proses: menentukan apakah mahasiswa tergolong mencapai KKM atau tidak 
#output: memperlihatkan hasil apakah mencapai KKM atau tidak

mahasiswa = int(input("Jumlah mahasiswa : "))
for i in range(1,mahasiswa+1):
    nilai = int(input("Mahasiswa {} mendapatkan nilai : ".format(i)))
    if nilai < 70:
        print("Nilai anda berada di bawah KKM. Mohon untuk mempelajari ulang materi.")
    elif nilai <= 80:
        print("Nilai anda berada di atas KKM. Pahamilah kembali apa yang salah dalam pengerjaan anda.")
    elif nilai <= 99:
        print("Nilai anda berada di atas KKM. Pahami sedikit lagi apa yang masih salah dalam pengerjaan anda.")
    elif nilai == 100:
        print("Nilai anda berada di atas KKM. Kamu sudah memahami semua materi yang diberikan, PERTAHANKAN.")
    else:
        print("Maaf sepertinya anda salah dalam menulis nilai")



