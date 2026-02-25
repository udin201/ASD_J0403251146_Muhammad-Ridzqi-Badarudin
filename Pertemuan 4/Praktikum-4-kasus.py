#====================================
#Nama   : Muhammad Ridzqi Badarudin
#NIM    : J0403251146
#Kelas  : B
#====================================

#====================================
#Studi kasus : Sistem Antrian Layanan Akademik
#Implementasi Queue =>
#Enqueue : Memindahkan pointer rear (nambah data baru di belakang)
#Dequeue : Memindahkan pointer front (menghapus data di depan)
#Front -> A -> B -> C -> Rear
#====================================

#1) Mendefinisikan Node (Unit dasar linked list)
class Node:
    def __init__(self, nim, nama):
        self.nim  = nim    #menyimpan nim mahasiswa
        self.nama = nama   #mewnyimpan nama mahasiswa
        self.next = None   #pointer ke node berikutnya

#2) Mendefinisikan queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        #ketika queue kosong maka front = rear = none
        return self.front is None
    #menambahkan data baru ke bagian belakang (rear)
    def enqueue(self, nim, nama):
        nodeBaru = Node(nim, nama) #instantiasi     
        #Jika data baru masuk dari queue yang kosong maka data baru = front = rear
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        #Jika queue tidak kosong, maka data baru diletakan setelah rear kemudian dijadikan sebagai rear
        self.rear.next = nodeBaru
        self.rear = nodeBaru

    #menghapus data paling depan (front)
    def dequeue(self):

        if self.is_empty():
            print("Antrian kosong. Tidak ada Mahasiswa yang dilayani")
            return None
        
        #lihat data bagian front, simpan di variabel data yang akan dihapus (dilayani)
        node_dilayani = self.front

        #geser pointer front ke next front
        self.front = self.front.next

        #jika front menjadi none (data antrian terakhir yang di layani), maka front = rear = none 
        if self.front is None:
            self.rear = None


        return node_dilayani
    
    def tampilkan(self):



        print("Daftar Antrian Mahasiswa (Front -> Rear) :")
        current = self.front
        no = 1
        while current is not None:
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next
            no += 1

#Program utama

def main():

    #instansiasi queue
    q = queueAkademik()

    while True:
        print("====== Sistem Antrian Akademik ======")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == '1':
            nim = input("Masukkan NIM : ").strip()
            nama = input("Masukkan Nama : ").strip()
            
            q.enqueue(nim, nama)
            print("Mahasiswa Berhasil Ditambahkan ke antrian.")

        elif pilihan == '2':
            dilayani = q.dequeue()
            print(f"Mahasiswa Dilayani : {dilayani.nama} - {dilayani.nim}")

        elif pilihan == '3':
            q.tampilkan()

        elif pilihan == '4':
            print("Program selesai. Terima kasih")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi 1-4")

#penanda eksekusi file utama
if __name__ == "__main__":
    main()