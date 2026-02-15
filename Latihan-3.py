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
# Single Linked List
# ==========================
class LinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan node di akhir
    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Menampilkan isi linked list
    def display(self):
        if not self.head:
            print("kosong")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # ==========================
    # LATIHAN 4 - Menggabungkan 2 Linked List
    # ==========================
    def merge(self, list2):
        merged_list = LinkedList()

        # Salin semua elemen dari list pertama
        temp = self.head
        while temp:
            merged_list.insert_at_end(temp.data)
            temp = temp.next

        # Salin semua elemen dari list kedua
        temp = list2.head
        while temp:
            merged_list.insert_at_end(temp.data)
            temp = temp.next

        return merged_list

# ==========================
# Program Utama
# ==========================

ll1 = LinkedList()
ll2 = LinkedList()

# Input Linked List 1
data1 = input("Masukkan elemen untuk Linked List 1 (pisahkan dengan koma): ")
if data1.strip() != "":
    elemen1 = data1.split(",")
    for item in elemen1:
        ll1.insert_at_end(int(item.strip()))

# Input Linked List 2
data2 = input("Masukkan elemen untuk Linked List 2 (pisahkan dengan koma): ")
if data2.strip() != "":
    elemen2 = data2.split(",")
    for item in elemen2:
        ll2.insert_at_end(int(item.strip()))

# Tampilkan Linked List 1
print("Linked List 1:", end=" ")
ll1.display()

# Tampilkan Linked List 2
print("Linked List 2:", end=" ")
ll2.display()

# Gabungkan
merged = ll1.merge(ll2)

# Tampilkan hasil gabungan
print("Linked List setelah digabungkan:", end=" ")
merged.display()