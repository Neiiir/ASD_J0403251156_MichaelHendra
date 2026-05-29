# ==========================================================
# Nama  : MICHAEL HENDRA
# NIM   : J0403251156
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# ==========================================================
# Jawaban Analisis:
#
# 1. Graph awal memiliki lebih banyak edge dan dapat
#    membentuk cycle, sedangkan spanning tree hanya
#    menghubungkan semua node tanpa cycle.
#
# 2. Spanning tree tidak boleh memiliki cycle karena
#    cycle menyebabkan penggunaan edge berlebih dan
#    membuat koneksi tidak efisien.
#
# 3. Jumlah edge spanning tree lebih sedikit karena
#    spanning tree hanya membutuhkan n-1 edge untuk
#    menghubungkan seluruh node.
# ==========================================================# ==========================================================
# Nama  : (Isi Nama Anda)
# NIM   : (Isi NIM Anda)
# Kelas : (Isi Kelas Anda)
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

print("Edge pada graph:")
for edge in edges:
    print(edge)

print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))

# ==========================================================
# Jawaban Analisis:
#
# 1. Graph awal memiliki lebih banyak edge dan dapat
#    membentuk cycle, sedangkan spanning tree hanya
#    menghubungkan semua node tanpa cycle.
#
# 2. Spanning tree tidak boleh memiliki cycle karena
#    cycle menyebabkan penggunaan edge berlebih dan
#    membuat koneksi tidak efisien.
#
# 3. Jumlah edge spanning tree lebih sedikit karena
#    spanning tree hanya membutuhkan n-1 edge untuk
#    menghubungkan seluruh node.
# ==========================================================