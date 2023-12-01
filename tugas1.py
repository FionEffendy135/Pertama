def pertama(awal,akhir):
    for i in range(awal, akhir + 1):
        if i%2 == 1:
            print(i)
    
def kedua(awal,akhir):
    for i in range(awal, akhir + 1):
        if i%2 == 0:
            print(i)

while True :
    print("Menu Pilihan :")
    print("1. Bilangan Ganjil")
    print("2. Bilangan Genap")
    print("3. Keluar")
    print("Silahkan Pilih Nomor")

    masukan = input("Pilih salah satu pilihan : ")
    if masukan == '1' or masukan == '2':
        awal = int(input("Masukkan Angka Awal : "))
        akhir = int(input("Masukkan Angka Akhir : "))

        if masukan == '1':
            pertama(awal,akhir)
        else:
            kedua(awal,akhir)
        

    elif masukan == '3':
        exit("Terima Kasih, Menutup Aplikasi")

    else:
        print("intput tidak valid")
