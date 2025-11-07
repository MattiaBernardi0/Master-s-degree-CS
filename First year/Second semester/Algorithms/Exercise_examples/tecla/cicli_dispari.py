#!/usr/bin/python3

# Matricola: VR502842

from collections import defaultdict
from collections import deque

def ricerca_cicli_dispari(grafo, nodo_sorgente, n, colorArr):
    # OSSERVAZIONE: Un grafo NON contiene un ciclo di lunghezza dispari solamente se il grafo è bipartito 
    #               -> per avere un ciclo dispari, due vertici dello stesso insieme devono essere connessi
    
    colorArr[nodo_sorgente] = 1
    q = deque()  # Creiamo una coda FIFO 
    q.append(nodo_sorgente)
    
    # L'idea è di ciclare sui vertici della coda in modo simile alla visita BFS
    while q:
        u = q.popleft()
        for v in grafo[u]:
            if colorArr[v] == -1:  # Se il nodo destinazione 'v' non è colorato, allora lo coloro con il colore opposto di 'u'
                colorArr[v] = 1 - colorArr[u]
                q.append(v) # Aggiungo il nodo 'v' alla coda
            elif colorArr[v] == colorArr[u]:  # Se il nodo destinazione 'v' ha lo stesso colore di 'u', abbiamo trovato un ciclo dispari e di conseguenza ritorniamo True
                return True
            
    # Non abbiamo trovato un ciclo di lunghezza dispari nel grafo e di conseguenza restituiamo False
    return False    

# Lettura dell'input
T = int(input())  # Numero di test case
for _ in range(T):
    n, m = map(int, input().split())  # Leggo il numero di nodi (n) e il numero di archi (m)
    grafo = defaultdict(list)  # Andiamo a creare il grafo

    for __ in range(m):  # Cicliamo sul numero di archi
        u, v = map(int, input().split())
        grafo[u].append(v)  # Aggiungo l'arco che vi è tra la coppia di nodi u-v
        grafo[v].append(u)  # NB!! Ho inserito l'arco da entrambe le direzioni, perchè il grafo non è diretto

    # Verifica della presenza di cicli dispari
    colorArr = [-1] * n # Inizializza l'array dei colori
    trovato_ciclo_dispari = False
    
    for nodo in range(n):
        if colorArr[nodo] == -1:  # Se il nodo non è colorato, significa che appartiene a una nuova componente connessa
            if ricerca_cicli_dispari(grafo, nodo, n, colorArr):
                trovato_ciclo_dispari = True
                break
    
