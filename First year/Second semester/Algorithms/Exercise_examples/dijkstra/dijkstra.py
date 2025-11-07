#!/usr/bin/python3
from collections import defaultdict
import heapq

T = int(input())    # Numero di test case
MOD = 1000000007

def dijkstra(grafo, n):
    distanza = [float('inf')] * n
    distanza[0] = 0 
    padre = [-1] * n
    padre[0] = 0
    numero_alberi = 1
    combinazioni = [1] * n
    
    min_heap = [(0, 0)]
    heapq.heapify(min_heap)
    while min_heap:
        distanza_corrente, u = heapq.heappop(min_heap)
        if distanza_corrente > distanza[u]:
            continue
        
        for v, peso in grafo[u]:
            if distanza[u] + peso < distanza[v]:
                distanza[v] = distanza[u] + peso
                heapq.heappush(min_heap, (distanza[v], v))
                padre[v] = u
            elif distanza[u] + peso == distanza[v]:
                if padre[v] > u:
                    padre[v] = u
    
    for i in range(n):
        numero_alberi *= combinazioni[i]
    
    return distanza, padre, numero_alberi
    
for _ in range(T):
    n, m = map(int, input().split())    # Leggo il numero di nodi (n) e il numero di archi (m)
    grafo = defaultdict(list)   # Creiamo il grafo    
    for __ in range(m):
        u, v, w = map(int, input().split())
        grafo[u].append((v, w))  # Aggiungo l'arco che vi è tra la coppia di nodi u-v con il relativo peso 'w' -> NB!! Non inserisco anche grafo[v].append(u), perchè il grafo è diretto
        
    # L'idea è di utilizzare l'algoritmo dijkstra, che permette di cercare i cammini minimi in un grafo con o senza ordinamento, ciclico e con pesi 
    # non negativi sugli archi. 
    distanza, padre, alberi = dijkstra(grafo, n)
    # Primo goal -> distanze d(0, 0), d(0, 1), ..., d(0, n - 1)
    output_distanza = " ".join(map(str, distanza))
    print(output_distanza)
    # Secondo goal -> padre dei cammini minimi, specificando il padre di ogni nodo
    output_padre = " ".join(map(str, padre))
    print(output_padre)
    # Terzo goal -> resto della divisione che ha il numero di alberi dei cammini minimi come dividendo e 1.000.000.007 come divisore
    numero_alberi = alberi % MOD
    print(numero_alberi)