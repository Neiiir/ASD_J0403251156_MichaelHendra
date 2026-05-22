# ==========================================================
# Nama :
# NIM :
# Kelas :
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================

# ==========================================================
# Latihan 2: Implementasi Dijkstra
# ==========================================================

import heapq

# Weighted graph dengan bobot positif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Priority queue menyimpan pasangan (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak lebih besar dari yang tersimpan, dilewati
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga
        for neighbor, weight in graph[current_node].items():

            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

hasil = dijkstra(graph, 'A')

print("Jarak terpendek dari node A:")

for node, distance in hasil.items():
    print(node, "=", distance)

# ==========================================================
# Jawaban Analisis:
# 1. Jarak terpendek dari A ke B adalah 4.
# 2. Jarak terpendek dari A ke C adalah 2.
# 3. Jarak terpendek dari A ke D adalah 3.
# 4. Karena jalur A -> C -> D memiliki total bobot
#    2 + 1 = 3, sedangkan A -> B -> D = 9.
# 5. Fungsi priority_queue adalah memilih node dengan
#    jarak terkecil terlebih dahulu agar proses lebih efisien.
# 6. Dijkstra tidak cocok untuk bobot negatif karena
#    algoritma ini menganggap jarak terpendek yang sudah
#    dipilih tidak akan berubah lagi.
# ==========================================================