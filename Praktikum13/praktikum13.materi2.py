# ==========================================================
# Nama  : MICHAEL HENDRA
# NIM   : J0403251156
# Kelas : TPL A1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):

    visited = set([start])
    edges = []

    # Menambahkan edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:

        # Mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        # Jika node belum dikunjungi
        if v not in visited:

            visited.add(v)

            # Menambahkan edge ke MST
            mst.append((u, v, weight))
            total_weight += weight

            # Menambahkan edge baru ke priority queue
            for neighbor, w in graph[v].items():

                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight


# Menjalankan algoritma Prim mulai dari node A
mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("Total bobot =", total)