# =============================
# Nama : Muhammad Ridzqi Badarudin
# NIM  : J0403251146
# =============================

# ==============================
# Membuat Node
# ==============================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# ==============================
# Membuat Linked List
# ==============================
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
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    # ==============================
    # LATIHAN 1
    # Menghapus node berdasarkan nilai tertentu
    # ==============================
    def delete_node(self, key):
        temp = self.head

        # Jika node pertama yang ingin dihapus
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None

        # Mencari node yang akan dihapus
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # Jika nilai tidak ditemukan
        if temp is None:
            print("Nilai tidak ditemukan dalam Linked List.")
            return

        # Menghapus node
        prev.next = temp.next
        temp = None


# ==============================
# Contoh Penggunaan
# ==============================

ll = LinkedList()

ll.insert_at_end(3)
ll.insert_at_end(5)
ll.insert_at_end(10)
ll.insert_at_end(2)

print("Linked List sebelum dihapus:")
ll.display()

ll.delete_node(10)

print("Linked List setelah menghapus 10:")
ll.display()