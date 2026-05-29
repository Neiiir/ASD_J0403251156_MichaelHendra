# ==========================================================
# Nama  : Michael Hendra
# NIM   : J0403251156
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# Kasus 1 : Jaringan Jalan Antar Kota
# Menggunakan Algoritma Kruskal

edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# Mengurutkan edge
edges.sort()

mst = []
total_weight = 0
connected = set()

for weight, u, v in edges:

    if u not in connected or v not in connected:

        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot minimum =", total_weight)

# ==========================================================
# Jawaban Analisis:
#
# 1. Kasus yang dipilih adalah jaringan jalan antar kota.
#
# 2. Algoritma yang digunakan adalah Kruskal.
#
# 3. Edge yang dipilih:
#    - Bogor - Depok = 2
#    - Depok - Jakarta = 3
#    - Depok - Bandung = 4
#
# 4. Total bobot MST adalah 9.
#
# 5. Edge tertentu tidak dipilih karena
#    memiliki bobot lebih besar dan dapat
#    membuat total biaya menjadi tidak minimum.
# ==========================================================