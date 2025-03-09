jumlah_uang = int(input("Total uang: "))
total_belanja = int(input("Total belanja: "))

if total_belanja > 100000:
    diskon = total_belanja * 0.10
    print("Dapat diskon 10%:", int(diskon))
elif total_belanja > 50000:
    diskon = total_belanja * 0.05
    print("Dapat diskon 5%:", int(diskon))
else:
    diskon = 0  
    print("Tidak dapat diskon")
total_setelah_diskon = total_belanja - diskon
print("Total yang harus dibayar:", int(total_setelah_diskon))
