class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete_node(self, key):
        temp = self.head

        # Jika node pertama yang dihapus
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Elemen tidak ditemukan.")
            return

        prev.next = temp.next
        temp = None

    def display(self):
        if not self.head:
            print("kosong")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


# =====================
# INPUT USER
# =====================

ll = LinkedList()

data = input("Masukkan elemen Linked List (pisahkan dengan koma): ")

if data.strip() != "":
    for x in data.split(","):
        ll.insert_at_end(int(x))

print("\nLinked List sebelum dihapus:")
ll.display()

key = int(input("Masukkan elemen yang ingin dihapus: "))

ll.delete_node(key)

print("\nLinked List setelah dihapus:")
ll.display()
