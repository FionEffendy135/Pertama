while True :
    print("Menu Pilihan :")
    print("1. Bilangan Ganjil")
    print("2. Bilangan Genap")
    print("3. Keluar")
    print("Silahkan Pilih Nomor")

    
    def pertama():
        awal = int(input("Masukkan Angka Awal : "))
        akhir = int(input("Masukkan Angka Akhir : "))
        for i in range(awal, akhir + 1):
            if i%2 == 1:
                print(i)
    
    def kedua():
        awal = int(input("Masukkan Angka Awal : "))
        akhir = int(input("Masukkan Angka Akhir : "))
        for i in range(awal, akhir + 1):
            if i%2 == 0:
                print(i)
    
    def ketiga():
        exit()
    

    masukan = input("Pilih salah satu pilihan : ")

    
    if masukan == '1':
        pertama()
        
    elif masukan == '2':
        kedua()

    elif masukan == '3':
        ketiga()

    else:
        print("intput tidak valid")