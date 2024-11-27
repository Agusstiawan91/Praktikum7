# Penjelasan program Praktikum7
Program Input Nilai

program dimulai dengan menampilkan menu pilihan : Lihat, Tambah, Ubah, Hapus, Cari, dan Keluar data.
1. Lihat Data (L):

   Menampilkan tabel daftar data mahasiswa yang telah dimasukkan dengan mencakup (NO, NIM, Nama, Nilai Tugas, UTS, UAS, dan Nilai AKhir) yang akan dihitung berdasarkan rumus tertentu.

   Nilai akhir dihitung dengan rumus:

   AKHIR = 0.3 × TUGAS + 0.3 × UTS + 0.4 × UAS

   Jika data kosong, maka program akan menampilkan "TIDAK ADA DATA".

3. Tambah Data (T):

   Memasukkan data baru mahasiswa berupa NIM, nama, nilai tugas, nilai UTS, dan nilai UAS. Setelah data dimasukkan, data tersebut disimpan dalam list data_mahasiswa dalam bentuk dictionary.
4. Ubah Data (U):

   Menampilkan data yang ada dan memungkinkan pengguna untuk memilih nomor data yang ingin diubah.
   Setelah memilih data yang akan diubah, pengguna dapat mengubah NIM, nama, atau nilai tugas, UTS, dan UAS. Jika data yang dimasukkan kosong, data sebelumnya akan tetap dipertahankan.
5. Hapus Data (H):

   Menampilkan data yang ada dan memungkinkan pengguna untuk memilih nomor data yang ingin dihapus.
   Setelah memilih data yang akan dihapus, data tersebut akan dihapus dari list data_mahasiswa.
6. Cari Data (C):

   Memungkinkan pengguna untuk mencari data berdasarkan NIM. Jika ditemukan, data mahasiswa tersebut akan ditampilkan.

   Jika NIM tidak ditemukan, program akan menampilkan pesan "Data tidak ditemukan."
8. Keluar Program (K):

   Mengakhiri program dan menampilkan pesan terima kasih.

# Flowchart
