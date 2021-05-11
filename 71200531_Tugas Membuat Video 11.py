#Terdapat 2 genre film yaitu adventure dan action. Film-film bergenre adventure
#yaitu Ready Player One, The SpongeBob Movie: Sponge on the Run, Aquaman, dan
#Now You See Me. Film-film bergenre action yaitu Ready Player One, Aquaman, dan
#Now You See Me. Dari 2 list tersebut Sako diminta membuat program yang dapat
#mengelompokkan film mana yang terdapat di 2 genre tersebut.
#Input : adventure dan action
#Proses : membuat set yang didalamnya terdapat film yang sama diantara adventure
#dan action
#Output : menghasilkan set tersebut
jumlah = int(input("Masukkan jumlah film genre adventure :"))
jumlah2 = int(input("Masukkan jumlah film genre action :"))
adventure = set()
action = set()
lst1 = []
lst2 = []
print("Masukkan film genre adventure:")
for i in range(jumlah):
    film1 = str(input())
    petualangan = lst1.append(film1)
print("Masukkan film genre action:")
for i in range(jumlah2):
    film2 = str(input())
    action = lst2.append(film2)
adventure = set(lst1)
action = set(lst2)
irisan = adventure & action
print("Film yang ada di 2 genre tersebut adalah:")
print(irisan)
