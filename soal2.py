print("===== Selamat datang di XXV =====")
ganjel = (1,3,5,7,9,11,13,15,17,19,21,24,25,27,29,31)
rego = 25000
dino = input("Masukkan tanggal hari ini: ")

if (dino == ganjel):
    print("== Berikut genre film yang tersedia ==")
    print("1. Horror")
    print("2. Action")
    genre = input("Silahkan pilih mau nonton film bergenre apa : ")
    if (genre == "1"):
        print("== Berikut pilihan film horror yang sedang tayang ==")
        print("1. The Devil's Light")
        print("2. Pengabdi Setan")
        film = input("Silahkan mau nonton film apa :")
        tiket = input("Mau memesan tiket sebanyak : ")
        print("Total yang harus dibayar adalah RP. ", int(tiket)*rego)
    elif (genre == "2"):
        print("== Berikut pilihan film action yang sedang tayang ==")
        print("1. Black Panther: Wakanda Forever")
        print("2. Avatar: The Way of Water")
        film = input("Silahkan mau nonton film apa :")
        tiket = input("Mau memesan tiket sebanyak : ")
        if (tiket > "4"):
            print("Total yang harus dibayar adalah Rp. ", int(tiket)*rego*0.95)
        else:
            print("Total yang harus dibayar adalah Rp. ", int(tiket)*rego)
    else:
        print("Pilihan yang anda pilih tidak tersedia di bioskop ini")
else:
    print("== Berikut genre film yang tersedia ==")
    print("1. Horror")
    print("2. Action")
    genre = input("Silahkan pilih mau nonton film bergenre apa : ")
    if (genre == "1"):
        print("== Berikut pilihan film horror yang sedang tayang ==")
        print("1. The Devil's Light")
        print("2. Pengabdi Setan")
        film = input("Silahkan mau nonton film apa :")
        tiket = input("Mau memesan tiket sebanyak : ")
        print("Total yang harus dibayar adalah Rp. ", int(tiket)*rego*0.98)
    elif (genre == "2"):
        print("== Berikut pilihan film action yang sedang tayang ==")
        print("1. Black Panther: Wakanda Forever")
        print("2. Avatar: The Way of Water")
        film = input("Silahkan mau nonton film apa :")
        tiket = input("Mau memesan tiket sebanyak : ")
        print("Total yang harus dibayar adalah Rp. ", int(tiket)*rego)
    else:
        print("Pilihan yang anda pilih tidak tersedia di bioskop ini")
