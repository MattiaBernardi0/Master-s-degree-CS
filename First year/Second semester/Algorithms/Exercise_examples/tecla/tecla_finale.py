#!/usr/bin/python3

# Matricola: VR502842

from collections import defaultdict
import sys
sys.setrecursionlimit(10*9)    




# Lettura dell'input
T = int(input())  # Numero di test case
for _ in range(T):
    n, m = map(int, input().split())  # Leggo il numero di nodi (n) e il numero di archi (m)
    grafo = defaultdict(list)  # Andiamo a creare il grafo

    for __ in range(m):  # Cicliamo sul numero di archi
        u, v = map(int, input().split())
        grafo[u].append(v)  # Aggiungo l'arco che vi è tra la coppia di nodi u-v
        grafo[v].append(u)  # NB!! Ho inserito l'arco da entrambe le direzioni, perchè il grafo non è diretto

    DFS(0, 0, -1)