# program input nilai
print("Program Input Nilai")
print("===================")

def tampilkan_tabel(data):
    print("\nDaftar Nilai")
    print("===================================")
    print("| NO |    NIM    |   NAMA   | TUGAS | UTS | UAS | AKHIR |")
    print("=========================================================")
    if not data:
        print("| TIDAK ADA DATA")
    else:
        for i, d in enumerate(data, start=1):
            akhir = (d['tugas'] * 0.3) + (d['uts'] * 0.3) + (d['uas'] * 0.4)
            print(f"| {i:<2} | {d['nim']:<8} | {d['nama']:<8} | {d['tugas']:<4} | {d['uts']:<3} | {d['uas']:<3} | {akhir:<5.2f} |")
    print("\n===================================")

def tambah_data(data):
    print("\nTambah Data")
    nim = input("NIM: ")
    nama = input("Nama: ")
    tugas = int(input("Nilai Tugas: "))
    uts = int(input("Nilai UTS: "))
    uas = int(input("Nilai UAS: "))
    
    data.append({'nim': nim, 'nama': nama, 'tugas': tugas, 'uts': uts, 'uas': uas})
    print("\nData berhasil ditambahkan!")

def ubah_data(data):
    print("\nUbah Data")
    tampilkan_tabel(data)
    no = int(input("Pilih nomor data yang ingin diubah: "))
    if 1 <= no <= len(data):
        data_ke = data[no - 1]
        print(f"Data yang dipilih: {data_ke}")
        data_ke['nim'] = input(f"NIM ({data_ke['nim']}): ") or data_ke['nim']
        data_ke['nama'] = input(f"Nama ({data_ke['nama']}): ") or data_ke['nama']
        data_ke['tugas'] = int(input(f"Nilai Tugas ({data_ke['tugas']}): ") or data_ke['tugas'])
        data_ke['uts'] = int(input(f"Nilai UTS ({data_ke['uts']}): ") or data_ke['uts'])
        data_ke['uas'] = int(input(f"Nilai UAS ({data_ke['uas']}): ") or data_ke['uas'])
        print("\nData berhasil diubah!")
    else:
        print("\nNomor tidak valid.")

def hapus_data(data):
    print("\nHapus Data")
    tampilkan_tabel(data)
    no = int(input("Pilih nomor data yang ingin dihapus: "))
    if 1 <= no <= len(data):
        data.pop(no - 1)
        print("\nData berhasil dihapus!")
    else:
        print("\nNomor tidak valid.")

def cari_data(data):
    print("\nCari Data")
    nim = input("Masukkan NIM yang dicari: ")
    found = [d for d in data if d['nim'] == nim]
    if found:
        print("\nData ditemukan:")
        tampilkan_tabel(found)
    else:
        print("\nData tidak ditemukan.")

def main():
    data_mahasiswa = []

    while True:
        print("\n[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]: ", end="")
        pilihan = input().lower()

        if pilihan == 'l':
            tampilkan_tabel(data_mahasiswa)
        elif pilihan == 't':
            tambah_data(data_mahasiswa)
        elif pilihan == 'u':
            ubah_data(data_mahasiswa)
        elif pilihan == 'h':
            hapus_data(data_mahasiswa)
        elif pilihan == 'c':
            cari_data(data_mahasiswa)
        elif pilihan == 'k':
            print("\nTerima kasih telah menggunakan program ini.")
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
