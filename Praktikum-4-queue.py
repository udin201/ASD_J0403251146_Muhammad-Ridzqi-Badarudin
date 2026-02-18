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

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        # Menambah data di belakang (rear)
        nodeBaru = Node(data)
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        #jika queue tidak kosong:
        #Rear lama menunjuk ke node baru
        self.rear.next = nodeBaru  
        self.rear = nodeBaru

        def dequeue(self):
            # Menghapus data dari depan
            
            
            #1) Lihat data yang paling depan
            data_terhapus = self.front.data

            #2) Geser front ke node berikutnya
            self.front = self.front.next

            #3) Jika setelah geser front menjaddi none, maka queue kosong
            #rear juga harus jadi none
            if self.front is None:
                self.rear = None

            return data_terhapus

    def tampilkan(self):
        #Menampilkan isi queue dari front ke rear
        current = self.front
        print("Front -> ", end="")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None  (Rear di node terakhir)")

    def dequeue(self):
        # Menghapus data dari depan (front) dan mengembalikan nilainya
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        nilai = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return nilai

    def peek(self):
        # Lihat elemen paling depan tanpa menghapus
        if self.is_empty():
            return None
        return self.front.data

    #Instantiasi obejek class QueueLL
q = QueueLL()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()

q.dequeue()
q.tampilkan()


