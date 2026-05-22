# ==========================================================
# Nama  : Michael Hendra
# NIM   : J0403251156
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# ==========================================================
# Latihan 5: Studi Kasus Shortest Path Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Representasi weighted graph antar kota
# Format:
# 'Kota Asal' : {'Kota Tujuan': bobot}
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

def dijkstra(graph, start):

    # Membuat dictionary untuk menyimpan jarak minimum
    # Semua node awalnya bernilai tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak node awal ke dirinya sendiri = 0
    distances[start] = 0

    # Priority queue untuk menyimpan node yang akan diproses
    # Format: (jarak, node)
    priority_queue = [(0, start)]

    # Perulangan selama queue masih memiliki isi
    while priority_queue:

        # Mengambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak lebih besar dari yang tersimpan, lewati
        if current_distance > distances[current_node]:
            continue

        # Memeriksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():

            # Menghitung jarak baru
            distance = current_distance + weight

            # Jika ditemukan jarak yang lebih kecil
            if distance < distances[neighbor]:

                # Update jarak minimum
                distances[neighbor] = distance

                # Masukkan ke priority queue
                heapq.heappush(priority_queue, (distance, neighbor))

    # Mengembalikan hasil jarak minimum
    return distances

# Menentukan node awal
start_node = 'Bogor'

# Menjalankan algoritma Dijkstra
hasil = dijkstra(graph, start_node)

# Menampilkan hasil
print("Jarak terpendek dari Bogor:")

for kota, jarak in hasil.items():
    print(f"Bogor -> {kota} = {jarak}")

# ==========================================================
# Jawaban Analisis:
#
# 1. Node awal yang digunakan adalah Bogor.
#
# 2. Node yang memiliki jarak paling kecil dari node awal
#    adalah Depok dengan jarak 2.
#
# 3. Node yang memiliki jarak paling besar dari node awal
#    adalah Bandung dengan jarak 8.
#
# 4. Algoritma Dijkstra bekerja dengan memilih node yang
#    memiliki jarak paling kecil terlebih dahulu, lalu
#    memperbarui jarak ke node tetangganya sampai semua
#    node mendapatkan jarak minimum.
#
# ==========================================================