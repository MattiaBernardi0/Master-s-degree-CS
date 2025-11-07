#!/usr/bin/python3

# Matricola: VR502842

from collections import defaultdict
from collections import deque

def ricerca_cicli_dispari(grafo, nodo_sorgente, n, colorArr):
    # OSSERVAZIONE: Un grafo NON contiene un ciclo di lunghezza dispari solamente se il grafo è bipartito 
    #               -> per avere un ciclo dispari, due vertici dello stesso insieme devono essere connessi
    
    colorArr[nodo_sorgente] = 1
    q = deque([(nodo_sorgente, [nodo_sorgente])])  # Creiamo una coda FIFO, in cui il primo elemento è il nodo 0, mentre il 2° elemento è una lista vuota 
    
    #ciclo_dispari_migliore = None
    ciclo_dispari = []  # Lista per memorizzare il ciclo dispari che troviamo all'interno del grafo
    
    # L'idea è di ciclare sui vertici della coda in modo simile alla visita BFS
    while q:
        u, ciclo_dispari = q.popleft()
        #ciclo_dispari.append(u)
        for v in grafo[u]:
            if colorArr[v] == -1:  # Se il nodo destinazione 'v' non è colorato, allora lo coloro con il colore opposto di 'u'
                colorArr[v] = 1 - colorArr[u]
                q.append((v, ciclo_dispari + [v])) # Aggiungo il nodo 'v' alla coda
            elif colorArr[v] == colorArr[u]:  # Se il nodo destinazione 'v' ha lo stesso colore di 'u', abbiamo trovato un ciclo dispari e di conseguenza ritorniamo True
                return ciclo_dispari + [v, ciclo_dispari[0]]
            
    # Non abbiamo trovato un ciclo di lunghezza dispari nel grafo e di conseguenza restituiamo False
    return []    

# Lettura dell'input
T = int(input())  # Numero di test case
for _ in range(T):
    n, m = map(int, input().split())  # Leggo il numero di nodi (n) e il numero di archi (m)
    grafo = defaultdict(list)  # Andiamo a creare il grafo

    for __ in range(m):  # Cicliamo sul numero di archi
        u, v = map(int, input().split())
        grafo[u].append(v)  # Aggiungo l'arco che vi è tra la coppia di nodi u-v
        grafo[v].append(u)  # NB!! Ho inserito l'arco da entrambe le direzioni, perchè il grafo non è diretto

    # Controllo se ci sono cicli dispari nel grafo
    colorArr = [-1] * n # Inizializza l'array dei colori
    nodi_ciclo = []
    nodi_ciclo = ricerca_cicli_dispari(grafo, 0, n, colorArr)

    if nodi_ciclo:
        print(len(nodi_ciclo))
        nodi_ciclo.append(0)
        print(" ".join(map(str, nodi_ciclo)))
    else:   # Non abbiamo trovato un ciclo dispari e di conseguenza stampo 0 su entrambe le righe
        print(len(nodi_ciclo))
        print(0)