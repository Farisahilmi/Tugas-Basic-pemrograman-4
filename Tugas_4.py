math = int(input("Masukkan nilai Matematika: "))
inggris = int(input("Masukkan nilai Inggris: "))
science = int(input("Masukkan nilai Science: "))

rata_rata = (math + inggris + science) / 3
dibawah_70 = (math < 70) + (inggris < 70) + (science < 70)

if math == 100 or inggris == 100 or science == 100:
    print("Karena ada satu mata pelajaran dengan nilai 100, kamu lulus!")
elif rata_rata > 75:
    print("Karena rata-rata nilai lebih dari 75, kamu lulus!")
elif dibawah_70 == 1:
    print("Karena hanya satu mata pelajaran di bawah 70, kamu lulus!")
else:
    print("Maaf, kamu tidak lulus.")

