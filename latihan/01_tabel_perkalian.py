# Program menampilkan tabel perkalian dari 1 sampai 10
# Perulangan for digunakan untuk menampilkan 10 hasil perkalian 

n = int(input("Bilangan: "))

for i in range(1, 11):
    hasil = n * i
    print(f"{n} x {i} = {hasil}")
