#====================================
#Nama   : Muhammad Ridzqi Badarudin
#NIM    : J0403251146
#Kelas  : B
#====================================

#====================================
#Impelementasi Dasar : Node pada Linked List
#====================================

#Membuat class Node(merupakan unit dasar dari linked list)
class Node:
    def __init__(self,data): #konstruktor
        self.data = data #menyimpan nilai/data
        self.next = None #pointer ke note berikutnya (awal=none)

# 1) Membuat node satu per satu
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

# 2) Menghubungkan Node : A -> B -> C -> None
nodeA.next = nodeB
nodeB.next = nodeC

# 3) Menentukan node pertama (head)
head = nodeA

# 4) Traversal : menelusuri dari head sampai none
current = head
while current is not None:
    print(current.data)    #menampilkan data node saat ini
    current = current.next #pindah ke node berikutnya

#===================================================
#Implementasi Dasar : Linked List + Insert Awal
#===================================================

class LinkedList:
    def __init__(self):
        self.head = None #awalnya kosong

    def insert_awal(self, data):
        #1) buat node baru
        nodeBaru = Node(data) #panggil class node

        #2) node baru menunjuk ke head lama
        nodeBaru.next = self.head 

        #3) head pindah ke node baru
        self.head = nodeBaru 

    def hapus_awal(self):
        data_terhapus = self.head.data #simpan data yang akan dihapus (opsional)
        self.head = self.head.next #head pindah ke node berikutnya
        print("Node yang dihapus adalah:", data_terhapus)

    def tampilkan(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


print("=== List Baru ===")
ll = LinkedList() #instasiasi objek ke class Linked List
ll.insert_awal("C")
ll.insert_awal("B")
ll.insert_awal("A")
ll.tampilkan()
print("\n=== Hapus Node Awal ===")
ll.hapus_awal()
print("\n=== List Setelah Hapus ===")
ll.tampilkan()  