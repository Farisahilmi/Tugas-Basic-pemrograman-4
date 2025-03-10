tahun = int(input("Masukkan tahun : "))

if (tahun % 400 == 0) or (tahun % 4 == 0):
    print("Tahun kabisat")
else:
    print("Bukan tahun kabisat")
