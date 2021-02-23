#Kasino diminta Dono untuk membuat perbandingan siapa yang tercepat dalam
#berlari 10 meter antara Dono, Kasino, dan Indro. Dono berlari 10 meter
#dalam waktu 15 detik, Kasino berlari 10 meter dalam waktu 17 detik
#dan Indro berlari 10 meter dalam waktu 13 detik.
#==============================================================================
# input : Dono, Kasino, Indro
# proses :   1. Jika Dono tercepat maka Dono < Kasino dan Dono < Indro
#           2. Jika Kasino tercepat maka Kasino < Dono dan Kasino < Indro
#           3. Jika Indro tercepat maka Indro < Kasino dan Indro < Dono
# Output : Menampilkan siapa yang tercepat diantara 3 orang tersebut
#==============================================================================

waktu1 = int(input("Waktu tempuh lari 10 meter orang 1(Dono)(detik) = "))
waktu2 = int(input("Waktu tempuh lari 10 meter orang 2(Kasino)(detik) = "))
waktu3 = int(input("Waktu tempuh lari 10 meter orang 3(Indro)(detik) = "))
if waktu1 < waktu2 and waktu1 < waktu3:
    print("Dono tercepat dengan waktu",waktu1,"detik")
elif waktu2 < waktu1 and waktu2 < waktu3:
    print("Kasino tercepat dengan waktu",waktu2,"detik")
elif waktu3 < waktu1 and waktu3 < waktu2:
    print("Indro tercepat dengan waktu",waktu3,"detik")
else:
    print("Yang tercepat tidak ditemukan")
