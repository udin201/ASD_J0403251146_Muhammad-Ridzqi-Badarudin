# ============================================================
# Praktikum Modul 1
# Studi Kasus: Manajemen Stok Barang (File Handling & Dictionary)
# ============================================================

# ------------------------------------------------------------
# FUNGSI: Membaca data stok barang dari file
# Data disimpan ke dictionary dengan key = KodeBarang
# ------------------------------------------------------------
def baca_data_barang(nama_file):
    data_barang = {}  # Dictionary untuk menyimpan data barang

    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            kode, nama, stok = baris.split(",")

            data_barang[kode] = {
                "nama": nama,
                "stok": int(stok)
            }

    return data_barang


# ------------------------------------------------------------
# FUNGSI: Menampilkan seluruh data barang
# ------------------------------------------------------------
def tampilkan_barang(data_barang):
    if len(data_barang) == 0:
        print("Data barang kosong.")
        return

    print("\n=== DAFTAR STOK BARANG ===")
    print("{:<8} | {:<15} | {:>5}".format("Kode", "Nama Barang", "Stok"))
    print("-" * 34)

    for kode in sorted(data_barang.keys()):
        nama = data_barang[kode]["nama"]
        stok = data_barang[kode]["stok"]
        print(f"{kode:<8} | {nama:<15} | {stok:>5}")


# ------------------------------------------------------------
# FUNGSI: Mencari barang berdasarkan kode
# ------------------------------------------------------------
def cari_barang(data_barang):
    kode = input("Masukkan kode barang: ").strip()

    if kode in data_barang:
        print("\nBarang ditemukan:")
        print("Kode :", kode)
        print("Nama :", data_barang[kode]["nama"])
        print("Stok :", data_barang[kode]["stok"])
    else:
        print("Barang tidak ditemukan.")


# ------------------------------------------------------------
# FUNGSI: Menambah barang baru
# ------------------------------------------------------------
def tambah_barang(data_barang):
    kode = input("Masukkan kode barang baru: ").strip()

    if kode in data_barang:
        print("Kode sudah digunakan.")
        return

    nama = input("Masukkan nama barang: ").strip()
    stok = int(input("Masukkan stok awal: "))

    data_barang[kode] = {
        "nama": nama,
        "stok": stok
    }

    print("Barang berhasil ditambahkan.")


# ------------------------------------------------------------
# FUNGSI: Update stok barang (tambah / kurangi)
# Stok tidak boleh negatif
# ------------------------------------------------------------
def update_stok(data_barang):
    kode = input("Masukkan kode barang: ").strip()

    if kode not in data_barang:
        print("Barang tidak ditemukan.")
        return

    print("1. Tambah stok")
    print("2. Kurangi stok")
    pilihan = input("Pilih opsi: ").strip()

    jumlah = int(input("Masukkan jumlah stok: "))

    if pilihan == "1":
        data_barang[kode]["stok"] += jumlah
        print("Stok berhasil ditambahkan.")

    elif pilihan == "2":
        if data_barang[kode]["stok"] - jumlah < 0:
            print("Stok tidak boleh negatif.")
        else:
            data_barang[kode]["stok"] -= jumlah
            print("Stok berhasil dikurangi.")

    else:
        print("Pilihan tidak valid.")


# ------------------------------------------------------------
# FUNGSI: Menyimpan data stok barang ke file
# ------------------------------------------------------------
def simpan_data(nama_file, data_barang):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in sorted(data_barang.keys()):
            nama = data_barang[kode]["nama"]
            stok = data_barang[kode]["stok"]
            file.write(f"{kode},{nama},{stok}\n")


# ------------------------------------------------------------
# FUNGSI UTAMA (MAIN PROGRAM)
# Menu interaktif menggunakan loop
# ------------------------------------------------------------
def main():
    nama_file = "stok_barang.txt"

    # Membaca data dari file saat program dimulai
    data_barang = baca_data_barang(nama_file)

    while True:
        print("\n=== MENU STOK BARANG ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tampilkan_barang(data_barang)

        elif pilihan == "2":
            cari_barang(data_barang)

        elif pilihan == "3":
            tambah_barang(data_barang)

        elif pilihan == "4":
            update_stok(data_barang)

        elif pilihan == "5":
            simpan_data(nama_file, data_barang)
            print("Data berhasil disimpan ke file.")

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


# ------------------------------------------------------------
# EKSEKUSI PROGRAM
# ------------------------------------------------------------
if __name__ == "__main__":
    main()