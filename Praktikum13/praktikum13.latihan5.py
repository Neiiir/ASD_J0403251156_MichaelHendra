# ==========================================================
# Nama  : Michael Hendra
# NIM   : J0403251156
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================


# ==========================================================
# Implementasi Algoritma Kruskal
# Kasus: Jaringan Komputer
# ==========================================================

# Daftar edge:
# (bobot, node1, node2)

edges = [
    (3, 'RouterA', 'RouterB'),
    (2, 'RouterA', 'RouterC'),
    (5, 'RouterB', 'RouterD'),
    (1, 'RouterC', 'RouterD'),
    (4, 'RouterB', 'RouterC')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0

# Menyimpan node yang sudah terhubung
connected = set()

for weight, u, v in edges:

    # Jika edge tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

# ==========================================================
# OUTPUT
# ==========================================================

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("\nTotal bobot minimum =", total_weight)

# ==========================================================
# Jawaban Analisis:
#
# 1. Kasus yang dipilih adalah jaringan komputer.
#
# 2. Algoritma yang digunakan adalah Kruskal.
#
# 3. Edge yang dipilih dalam MST:
#    - RouterC - RouterD = 1
#    - RouterA - RouterC = 2
#    - RouterA - RouterB = 3
#
# 4. Total bobot MST adalah 6.
#
# 5. Edge tertentu tidak dipilih karena
#    memiliki bobot lebih besar dan dapat
#    menyebabkan cycle sehingga tidak efisien.
# ==========================================================