#======================================
#praktium 1 konsep adt dan file handling
#latihan dasar 1 : membaca file teks
#=======================================

import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(script_dir, "data_mahasiswa.txt")

#membuka file dalam satu string
print("===Membuka file dalam satu string===")
with open(data_file,"r", encoding="utf-8") as file:
    isi_file = file.read() #membaca seluruh isi file
print(isi_file)
print("===Hasil Read===")
print("tipe data: ", type(isi_file))
print("Jumlah Karakter" , len(isi_file))
print("jumlah baris: ", isi_file.count("\n")+1)

#membuka file per baris
print("===Membaca file per baris===")
jumlah_baris = 0
with open(data_file,"r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip()
        print("Baris ke-", jumlah_baris) #strip() untuk menghilangkan karakter newline
        print("isi baris" , baris)

#======================================
#praktium 1 konsep adt dan file handling
#latihan dasar 2 : parsing baris menjadi kolom data
#=======================================
with open(data_file,"r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter newline
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan
        print("NIM:", nim, "Nama:", nama, "Nilai:", int(nilai))

#======================================
#praktium 1 konsep adt dan file handling
#latihan dasar 3 : membaca file dan menyimpan pada list
#=======================================
data_list = [] # List untuk menyimpan data mahasiswa

with open(data_file,"r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")

        #simpan sebagai list " [NIM, Nama, Nilai] "
        data_list.append([nim, nama, int(nilai)])

print("===Data Mahasiswa dalam bentuk List===")
print(data_list)

print("=== Jumlah Record ===")
print("Jumlah Record:", len(data_list))

print("=== menampilkan data record tertentu===")
print("contoh record pertama:", data_list[0])#array dimulai dari 0

#==============================
#praktikum 1 konsep adt dan file handling
#latihan dasar 4 : membaca file dan menyimpan pada dictionary
#==============================

data_dict = {} # Dictionary untuk menyimpan data mahasiswa
with open(data_file,"r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #menghilangkan karakter newline
        nim, nama, nilai = baris.split(",") #pecah menjadi data satuan

        #simpan sebagai dictionary dengan NIM sebagai key
        data_dict[nim] = {"nama": nama, "nilai": int(nilai)} 

print("===Data Mahasiswa dalam bentuk Dictionary===")
print(data_dict)