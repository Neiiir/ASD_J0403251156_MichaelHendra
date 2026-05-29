# ==========================================================
# Nama  : Michael Hendra
# NIM   : J0403251156
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# Studi Kasus:
# Jaringan Kabel Antar Gedung
# Menggunakan Algoritma Kruskal

# Daftar edge
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
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

print("Edge yang dipilih:")

for edge in mst:
    print(edge)

print("Total biaya minimum =", total_weight)

# ==========================================================
# Jawaban Analisis:
#
# 1. Algoritma yang digunakan adalah Kruskal.
#
# 2. Edge yang dipilih:
#    - GedungC - GedungD = 1
#    - GedungA - GedungC = 2
#    - GedungB - GedungD = 3
#
# 3. Total biaya minimum adalah 6.
#
# 4. MST cocok digunakan karena dapat
#    menghubungkan seluruh gedung dengan
#    biaya kabel minimum tanpa koneksi berlebih.
# ==========================================================