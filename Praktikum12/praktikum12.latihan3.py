# Nama  : Michael Hendra
# NIM   : J0403251156
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak awal = 0
    distances[start] = 0

    # Relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        for node in graph:
            for neighbor, weight in graph[node].items():

                if distances[node] != float('inf') and \
                   distances[node] + weight < distances[neighbor]:

                    distances[neighbor] = distances[node] + weight

    return distances

hasil = bellman_ford(graph, 'A')

print("Jarak terpendek dari node A:")

for node, distance in hasil.items():
    print(node, "=", distance)

# ==========================================================
# Jawaban Analisis:
# 1. Bobot langsung dari A ke B adalah 5.
# 2. Total bobot jalur A -> C -> B adalah 2.
# 3. Jalur yang lebih kecil menuju B adalah melalui C.
# 4. Bellman-Ford dapat digunakan pada graph berbobot
#    negatif karena melakukan relaksasi edge berulang.
# 5. Relaksasi edge adalah proses memperbarui jarak
#    menjadi lebih kecil jika ditemukan jalur yang lebih baik.
# 6. Dijkstra menggunakan pendekatan greedy dan tidak
#    mendukung bobot negatif, sedangkan Bellman-Ford
#    mendukung bobot negatif.
# ==========================================================