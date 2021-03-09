#Dosen meminta mahasiswa untuk membuat sebuah program untuk menghitung deret
#bilangan dari n sampai z. n = 3 dan z = 13.
#============================================================================
#input : n, z, total
#proses : total = penjumlahan antara n sampai dengan z
#output : hasil penjumlahan dari n sampai z yaitu total
#============================================================================

n = int(input("n(awal bilangan) = "))
z = int(input("z(banyak bilangan) = "))
total = 0
print("Deret bilangan: ",end='')
for i in range(n,z+1,1):
    if i == z:
        print("%d \n"%i,end='')
    else:
        print("%d + "%i,end='')
    total = total + i
print("Total perhitungan deret = %d"%(total))
