#=================================================
#Nama : Michael Hendra
#NIM  : J0403251156
#Kelas: A1
#=================================================

#=================================================
#Implementasi Dasar : Node pada Linked List
#=================================================

class Node:
    #Konstruktor yang dijalankan secara otomatis ketika class node diapnggil/diinstantiasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list/node
        self.next = None #pointer utk menunjuk ke note berikutnya (kalo di awal = None)

#1) Membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC= Node("C")

#2) Menghubungkan Node: A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = None

#3) (Traversal) : Menelusuri node dari head sampai ke None 
current = head
while current is not None:
    print(current.data) #Menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutnya