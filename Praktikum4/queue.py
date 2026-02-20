#=================================================
#Nama : Michael Hendra
#NIM  : J0403251156
#Kelas: A1
#=================================================

#=================================================
#Implementasi Dasar : Queue
#=================================================

class Node:
    #Konstruktor yang dijalankan secara otomatis ketika class Node diapnggil/diinstantiasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list/Node
        self.next = None #pointer utk menunjuk ke Node berikutnya (kalo di awal = None)

class queue:
    #buat konstruktor utk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang

    def is_empty(self):
        return self.front is None


    # Membuat fungsi utk menambahkan data baru ke bagian belakang
    def enqueue(self, data):
        nodeBaru = Node(data)
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        #jika queue tidak kosong, maka letakkan data baru ke setelah rear, dan jadikan data baru sebagai rear
        self.rear.next = nodeBaru #Letakkan data baru pada setelahnya rear
        self.rear = nodeBaru #Jadikan data baru sebagai rear

    def dequeue(self):
        #menghapus data dari depan/front
        data_terhapus = self.front.data #lihat data paling depan\

        #geser front ke node berikutnya
        self.front = self.front.next

        #jika setelah geser front menjadi none, maka queue kosong
        #rear juga harus jadi None
        if self.front is None:
            self.rear = None

        return data_terhapus
    
    def tampilkan(self):
        current = self.front
        print("Front ->", end=" ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print(" Rear ")


#Instantiasi class queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()