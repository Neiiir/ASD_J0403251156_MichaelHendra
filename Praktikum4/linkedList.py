#=================================================
#Nama : Michael Hendra
#NIM  : J0403251156
#Kelas: A1
#=================================================

#=================================================
#Implementasi Dasar : Node pada Linked List
#=================================================

class Node:
    #Konstruktor yang dijalankan secara otomatis ketika class Node diapnggil/diinstantiasi
    def __init__(self, data):
        self.data = data #menyimpan nilai atau data pada list/Node
        self.next = None #pointer utk menunjuk ke Node berikutnya (kalo di awal = None)

#1) Membuat node dengan instantiasi class Node
nodeA = Node("A")
nodeB = Node("B")
nodeC= Node("C")

#2) Mendefinisikan head dan Menghubungkan antar Node: A -> B -> C -> None
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = None #Tidak diperlukan

#3) (Traversal) : Menelusuri Node dari head sampai ke None
current = head
while current is not None:
    print(current.data) #Menampilkan data pada Node saat ini
    current = current.next #pindah ke Node berikutnya


