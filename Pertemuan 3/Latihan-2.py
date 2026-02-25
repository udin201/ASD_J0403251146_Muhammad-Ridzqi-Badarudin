# ==========================
# Nama : Muhammad Ridzqi Badarudin
# NIM  : J0403251146
# ==========================

# ==========================
# Membuat Node
# ==========================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ==========================
# Circular Singly Linked List
# ==========================
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Menambahkan node di akhir
    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:  # Jika list kosong
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head  # Circular link
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head  # Circular link kembali ke head

    # ==========================
    # LATIHAN 2 - Pencarian
    # ==========================
    def search(self, key):
        if not self.head:
            print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
            return

        temp = self.head

        # Cek node pertama
        if temp.data == key:
            print(f"Elemen {key} ditemukan dalam Circular Linked List.")
            return

        temp = temp.next

        # Loop sampai kembali ke head
        while temp != self.head:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Circular Linked List.")
                return
            temp = temp.next

        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")


# ==========================
# Program Utama
# ==========================

cll = CircularSinglyLinkedList()

# Input elemen
data_input = input("Masukkan elemen ke dalam Circular Linked List (pisahkan dengan koma): ")

if data_input.strip() != "":
    elemen = data_input.split(",")
    for item in elemen:
        cll.insert_at_end(int(item.strip()))

# Input nilai yang ingin dicari
cari = int(input("Masukkan elemen yang ingin dicari: "))

# Panggil fungsi pencarian
cll.search(cari)