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

    def display(self):
        if not self.head:
            print("kosong")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def merge(self, other):
        if not self.head:
            self.head = other.head
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = other.head


# =========================
# INPUT DARI USER
# =========================

ll1 = LinkedList()
ll2 = LinkedList()

# Input List 1
data1 = input("Masukkan elemen Linked List 1 (pisahkan dengan koma): ")

if data1.strip() != "":
    for x in data1.split(","):
        ll1.insert_at_end(int(x))

# Input List 2
data2 = input("Masukkan elemen Linked List 2 (pisahkan dengan koma): ")

if data2.strip() != "":
    for x in data2.split(","):
        ll2.insert_at_end(int(x))


# =========================
# OUTPUT
# =========================

print("\nLinked List 1:")
ll1.display()

print("Linked List 2:")
ll2.display()

ll1.merge(ll2)

print("Linked List setelah digabung:")
ll1.display()