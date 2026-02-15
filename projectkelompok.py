# 1. Definisi Struktur Data (Node)
class NodeBulan:
    def __init__(self, nama_bulan, tahun):
        self.nama_bulan = nama_bulan
        self.tahun = tahun
        self.transaksi = []  # List sederhana untuk simpan string transaksi
        self.next = None     # Pointer ke bulan depan
        self.prev = None     # Pointer ke bulan lalu

# 2. Fungsi untuk Menambah Transaksi (Input Manual)
def tambah_data(node, tgl, ket, nominal):
    data = f"{tgl} | {ket:<15} | Rp{nominal:>10}"
    node.transaksi.append(data)

# 3. Persiapan Data (Seolah-olah database)
januari = NodeBulan("Januari", 2026)
februari = NodeBulan("Februari", 2026)
maret = NodeBulan("Maret", 2026)

# Menyambungkan antar bulan (Doubly Linked List Manual)
januari.next = februari
februari.prev身 = januari
februari.next = maret
maret.prev = februari

# Isi Data Contoh (Dummy Data)
tambah_data(januari, "02/01", "Kiriman Ortu", 2000000)
tambah_data(januari, "10/01", "Bayar Kos", 800000)
tambah_data(februari, "05/02", "Beli Buku", 150000)
tambah_data(maret, "01/03", "Jajan Kopi", 50000)

# 4. Program Utama (Main Loop)
current = februari  # Mulai dari bulan Februari sebagai tampilan awal

while True:
    print("\n" + "="*40)
    print(f"MUTASI REKENING: {current.nama_bulan} {current.tahun}")
    print("="*40)
    
    if not current.transaksi:
        print("Belum ada transaksi.")
    else:
        for t in current.transaksi:
            print(t)
    
    print("-" * 40)
    print("Navigasi: [1] Bulan Lalu  [2] Bulan Depan  [0] Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        if current.prev is not None:
            current = current.prev
        else:
            print("\n>> Gagal: Ini sudah bulan paling awal!")
            
    elif pilihan == "2":
        if current.next is not None:
            current = current.next
        else:
            print("\n>> Gagal: Belum ada data bulan depan!")
            
    elif pilihan == "0":
        print("Terima kasih sudah menggunakan aplikasi ini!")
        break
    else:
        print("Pilihan tidak valid.")