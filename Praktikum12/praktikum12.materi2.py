# Nama  : Michael Hendra
# NIM   : J0403251156
# Kelas : TPL A1
# Praktikum 12 - Graph II: Shortest Path

# ==========================================================
# Implementasi Algoritma Bellman-Ford
# ==========================================================

def bellman_ford(graph, start):

    # Membuat dictionary untuk menyimpan jarak minimum
    # Semua node awalnya bernilai tak hingga (infinity)
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri = 0
    distances[start] = 0

    # Proses relaksasi dilakukan sebanyak jumlah node - 1
    # Tujuannya untuk memastikan semua jalur minimum ditemukan
    for _ in range(len(graph) - 1):

        # Memeriksa setiap node pada graph
        for node in graph:

            # Memeriksa seluruh tetangga dan bobot edge
            for neighbor, weight in graph[node].items():

                # Menghitung kemungkinan jarak baru
                # Jika lebih kecil dari jarak sebelumnya,
                # maka jarak diperbarui
                if distances[node] + weight < distances[neighbor]:

                    distances[neighbor] = distances[node] + weight

    # Mengembalikan hasil jarak minimum
    return distances