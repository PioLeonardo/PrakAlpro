#Suti ingin membuat program yang dapat mencatat buku perkuliahan apa saja yang
#dipunyainya sehingga dia dapat lebih mudah mengecek bukunya nanti di kamarnya.
#Buku2nya adalah sebagai berikut:(terdapat 3 buku)
#Discrete Mathematics and Its Applications 7th Edition, About Face: The
#Essentials of Interaction Design, Don’t Make Me Think Revisited: A Common Sense
#Approach to Web Usability
#Input : buku_perkuliahan
#Proses : Membuat fungsi yang dapat mengeluarkan buku yang ia simpan
#Output : List buku yang dipunyainya
def hitung(buku_perkuliahan):
    hitung = []
    for i in buku_perkuliahan:
        hitung.append(i)
    kunci = list(dict.fromkeys(hitung))
    out = {}
    for j in kunci:
        k = {x for x in hitung if x == j}
        out[j] = len(k)
    lst = list(out.items())
    total = 0
    for key,val in lst:
        total += val
        print("Buku Berjudul",key,"berjumlah",val,"buku.")
    print("Total buku perkuliahan Suti adalah",total,"buku.")
buku_perkuliahan =("Discrete Mathematics and Its Applications 7th Edition","About Face: The Essentials of Interaction Design","Don’t Make Me Think Revisited: A Common Sense Approach to Web Usability")
hitung(buku_perkuliahan)

