#=================================================
#Nama : Michael Hendra
#NIM  : J0403251156
#Kelas: A1
#=================================================

#=================================================
#Implementasi Dasar : Stack
#=================================================

class Node:
    #Konstruktor yang dijalankan secara otomatis ketika class Node diapnggil/diinstantiasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list/Node
        self.next = None #pointer utk menunjuk ke Node berikutnya (kalo di awal = None)

#Stack ada operasi push(memasukkan head baru) and pop(menghapus head)
# ILUSTRASI
# C -> None 
# Jika dimasukkan node B maka jadi B -> C -> None (yang dijalankan duluan B)

class stack: 
    def __init__(self):
        self.top = None #top menunjuk ke Node paling atas (awalnya kosong)
    
    def push(self, data): #Memasukkan data baru pada stack
        #1. Membuat Node baru
        nodeBaru = Node(data) #Instantiasi/memanggil konstruktor pada class Node

        #2. Node baru menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top

        #3. Geser top pindah ke node baru
        self.top = nodeBaru

        # B -> A -> None
    
    def is_empty(self):
        return self.top is None

    def pop(self): #Mengambil / menghapus Node paling atas (top/head)
        if self.is_empty():
            print("Stack kosong, tidak bisa pop")
            return None
        data_terhapus = self.top.data  #soroti bagian top dan simpan di variabel
        # B -> A -> None lalu akan menjadi A -> None
        self.top = self.top.next 
        return data_terhapus
        # Namun jika hanya tersisa 1 Node tidak bisa dipop

    def peek(self):
        #Melihat data yang paling atas tanpa menghapus 
        if self.is_empty():
            return None 
        return self.top.data


    def tampilkan(self):
        #Top -> A -> B
        current = self.top
        print("Top ->", end=" ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

#Instantiasi Class Stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek (Lihat top): ", s.peek())
s.pop()
s.tampilkan()
print("Peek (Lihat top): ", s.peek())

# s.pop()
# s.tampilkan()
# s.pop()
# s.tampilkan()
# s.pop()
# s.tampilkan()
# s.pop()
# s.tampilkan()
