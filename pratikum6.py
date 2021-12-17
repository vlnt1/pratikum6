data = {}

def tambah():
    print("Tambah Data")
    nama = input("Nama\t\t: ")
    nim = int(input("NIM\t\t\t: "))
    tugas = int(input("NIlai Tugas\t: "))
    uts = int(input("Nilai UTS\t: "))
    uas = int(input("Nilai UAS\t: "))
    nilaiakhir = (tugas * 0.3 + uts * 0.35 + uas * 0.35)
    data[nama] = nim, tugas, uts, uas, nilaiakhir


def tampilkan():
    if data.items():
        print("~~~~~~~~~~~~| Daftar Nilai |~~~~~~~~~~~~")
        print("_____________________________")
        print("|  No  |      NIM      |      NAMA         |    TUGAS   |   UTS   |   UAS   | AKHIR  |")
        print("|__|_____|______|____|___|___|__|_")
        i = 0
        for a in data.items():
            i += 1
            print(f"| {i:4} | {a[0]:13s} | {a[1][0]:17} | {a[1][1]:10d} |  {a[1][2]:6d} | {a[1][2]:7d} | {a[1][4]:6.2f} | ")
    else:
        print("~~~~~~~~~~~~| Daftar Nilai |~~~~~~~~~~~~")
        print("_____________________________")
        print("|  No  |      Nama     |      NIM      |   TUGAS  |   UTS   |   UAS   | Nilai Akhir  |")
        print("_____________________________")
        print("|      |               |             Tidak Ada Data         |         |                |")
    print("________________________________")


def hapus():
    print("Hapus Data Nilai Mahasiswa")
    nama = input(" Masukan Nama\t:")
    if nama in data.keys():
        del data[nama]
        print()
        print("~~~~~~~~~~~")
        print("===| BERHASIL MENGHAPUS DATA |===")
        print("~~~~~~~~~~~")
    else:
        print("Data {0} tidak ada".format(nama))


def ubah():
    print("~~~~~~~~~~~~~")
    print("===| Edit Data Nilai Mahasiswa |===")
    print("~~~~~~~~~~~~~")
    nama = input("Masukan Nama\t\t: ")
    print("_____________")
    if nama in data.keys():
        nim = input("NIM baru\t\t\t: ")
        tugas = int(input("Nilai Tugas Baru\t: "))
        uts = int(input("Nilai UTS Baru\t\t: "))
        uas = int(input("Nilai UAS Baru\t\t: "))
        nilaiakhir = (tugas * 30 / 100 + uts * 35 / 100 + uas * 35 / 100)
        data[nama] = nim, tugas, uts, uas, nilaiakhir
        print()
        print("<><><><><><><><><><><><><><><><>")
        print("====| BERHASIL MENGUBAH DATA |====")
        print("<><><><><><><><><><><><><><><><>")
    else:
        print("Data nilai {0} tidak ada ".format(nama))

while True:
    print("")
    print("|<><><><><><><><><><><><><><><><><>|")
    print("|~~~| DATA MAHASISWA |~~~|")
    print("|<><><><><><><><><><><><><><><><><>|")
    x = input("1.| Tambah \n2.| Tampilkan \n3.| Hapus Nama \n4.| Ubah Nama\n: ")
    if x.lower() == "1":
        tambah()
    elif x.lower() == "2":
        tampilkan()
    elif x.lower() == "3":
        hapus()
    elif x.lower() == "4":
        ubah()
    elif x.lower() == "0":
        print()
        print("    MICHAEL VALENTINO LAISINA    ")
        print("            312110045            ")
        print("            TI.21.C1             ")
        print("====== KELUAR DARI PROGRAM ======")
        break