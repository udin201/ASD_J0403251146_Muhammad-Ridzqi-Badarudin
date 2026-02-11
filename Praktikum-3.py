#=======================================
#praktikum 2 Konsep ADT dan File Handling
#latihan dasar 1 : Membuat fungsi load data
#=======================================

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
nama_file = os.path.join(script_dir, "data_mahasiswa.txt")

#membuat fungsi untuk membaca data mahasiswa
def baca_data_mahasiswa(nama_file):
  data_dict = {} #inisialisasi data dictionary
  with open(nama_file,"r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter newline

        parts = baris.split(",")
        if len(parts) != 3:
             continue  # lewati baris yang tidak sesuai format
        nim, nama, nilai_str = parts  #pecah menjadi data satuan
        nilai = int(nilai_str)  #konversi nilai ke integer
        data_dict[nim] = {
            "nama": nama, 
             "nilai": nilai
            } 
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan
    #simpan data dalam dictionary (key, value)
        data_dict[nim] = {
            "nama": nama, 
             "nilai": int(nilai)
            } 
    return data_dict

#memanggil fungsi untuk membaca data mahasiswa
buka_data = baca_data_mahasiswa(nama_file)
#print("jumlah data terbaca", len(buka_data))

#=======================================
#praktikum 2 Konsep ADT dan File Handling
#latihan dasar 2 : Membuat fungsi menampilkan data
#=======================================


def tampilkan_data(data_dict):
   
   if len(data_dict) == 0:
       print("Data kosong")
       return
   #Membuat Header Tabel
   print("\n===Data Mahasiswa===")
   print(f"{'NIM' : <10} | {'Nama':<12} | {'Nilai':>5}")
   print("-" * 32)

   '''
   untuk tampilan yang rapi, atur f-string formating
     {'NIM' : <10}  : rata kiri dengan lebar 10 karakter
     {'Nama':<12}  : rata kiri dengan lebar 12 karakter
     {'Nilai':>5}  : rata kanan dengan lebar 5 karakter
   '''

   for nim in sorted(data_dict):
       nama = data_dict[nim]["nama"]
       nilai = data_dict[nim]["nilai"]
       print(f"{nim : <10} | {nama:<12} | {nilai:>5}")

#memanggil fungsi untuk menampilkan data
#tampilkan_data(buka_data)

#=======================================
#praktikum 2 Konsep ADT dan File Handling
#latihan dasar 3 : Membuat fungsi mencari data
#=======================================

def cari_data(data_dict,):
   #mencari data mahasiswa berdasarkan NIM
    nim_cari = input("Masukkan NIM yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]
        print("\n==== Data Mahasiswa Ditemukan ====")
        print(f"NIM     : {nim_cari}")
        print(f"Nama    : {nama}")
        print(f"Nilai   : {nilai}")
    else:
        print("\nData tidak ditemukan")

#cari_data(buka_data)

#=======================================
#praktikum 2 Konsep ADT dan File Handling
#latihan dasar 4 : Membuat fungsi update nilai
#=======================================

def update_nilai(data_dict):

    #cari nim mahasiswa yang akan diupdate nilainya
    nim = input("Masukkan NIM mahasiwa yang akan diupdate nilainya ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan, update dibatalkan.")
        return
    try:
        nilai_baru = int(input("Masukkan nilai baru (0-100): ").strip())
    except ValueError:
        print("Nilai harus berupa angka, Update dibatalkan")
        return
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0-100. Update dibatalkan.")
        
    nilai_lama = data_dict[nim]["nilai"]
    #memasukan nilai update baru ke dictionary
    data_dict[nim]["nilai"] = nilai_baru

    print("Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#update_nilai(buka_data)

#=======================================
#praktikum 2 Konsep ADT dan File Handling
#latihan dasar 5 : Membuat fungsi menyimpan perubahan data ke file
#=======================================

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim},{nama},{nilai}\n")

#simpan_data(nama_file, buka_data)
#print("Data Berhasil Disimpan")

#=======================================
#praktikum 2 Konsep ADT dan File Handling
#latihan dasar 6 : Membuat Menu Program
#=======================================


def main():

    #menjalankan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)

while True:
    print("\n=== MENU DATA MAHASISWA ===")
    print("1. Tampilkan semua data")
    print("2. Cari data berdasarkan NIM")
    print("3. Update nilai mahasiswa")
    print("4. Simpan data ke file")
    print("0. Keluar")

    pilihan = input("Pilihan menu: ").strip()

    if pilihan == "1":
        tampilkan_data(buka_data)

    elif pilihan == "2":
        cari_data(buka_data)

    elif pilihan == "3":
        update_nilai(buka_data)

    elif pilihan == "4":
        simpan_data(nama_file, buka_data)
        print("Data berhasil disimpan")

    elif pilihan == "0":
        print("Program Selesai")
        break
    else:
        print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
 main()