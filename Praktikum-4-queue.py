#====================================
#Nama   : Muhammad Ridzqi Badarudin
#NIM    : J0403251146
#Kelas  : B
#====================================

#====================================
#Impelementasi Dasar : Node pada Linked List
#====================================

# Membuat class Node (merupakan unit dasar dari linked list)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueLL:
    def __init__(self):
        self.front = None  # Node paling depan
        self.rear = None   # Node paling belakang

    def enqueue(self, data):
        # Menambah data di belakang (rear)
        nodeBaru = Node(data)
        if self.is_empty(self):
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        self.rear.next = nodeBaru  # Rear menunjuk ke node baru
        #Rear pindah ke node baru
        self.rear = nodeBaru

    def tampilkan(self):
        #Menampilkan isi queue dari front ke rear
        current = self.front
        print("Front -> ", end="->")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None - Rear di node terakhir")

    #Instantiasi obejek class QueueLL
q = QueueLL()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()   

