#Sukar diminta untuk membuat program yang berfungsi mengukur percepatan motor milik 
#Sandi dengan kecepatan 80m/s selama 50 detik. Program yang dijalankan memerlukan
#inputan kecepatan, waktu, dan percepatan.
#==================================================================================
#input : kecepatan ; waktu ; percepatan
#proses : percepatan = kecepatan / waktu
#output : hasil dari percepatan(m/s^2)
#================================================================================
#input : Kecepatan = 80m/s
#       Waktu = 50 s
#       percepatan = 0
#proses : percepatan = kecepatan / waktu (80/50)
#output : hasil dari percepatan (m/s^2)
#==================================================================================
kecepatan = int(input("Masukkan kecepatan = "))
waktu = int(input("Masukkan waktu = "))
percepatan = kecepatan / waktu
print("Hasil dari percepatannya adalah = ",percepatan,"m/s^2")
