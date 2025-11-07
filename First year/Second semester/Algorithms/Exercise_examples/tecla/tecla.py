#!/usr/bin/python3
from collections import defaultdict
from collections import deque

def from_zero_to_zero(grafo, nodo_sorgente, n):
    # L'idea è di trovare un percorso che parta dal nodo 0 e ritorni al nodo 0 con Tecla che si trova nello stato SLURP
    # OSSERVAZIONI: - Per riuscirci dobbiamo trovare un percorso di lunghezza dispari e attarversiamo un nodo solamente se lo attraversiamo
    #                   in uno stato diverso rispetto alla volta precedente
    #               - Per riuscire a trovare il percorso migliore utilizzo una BFS
        
    # STATO STOMACO: BLEAH = 0  SLURP = 1    
    stato_iniziale = 0  # Inializzo lo stato iniziale dello stomaco di Tecla a BLEAH
    q = deque([(nodo_sorgente, stato_iniziale)])    # Creo una coda FIFO per gestire i nodi da esplorare
    visitati = set([(nodo_sorgente, stato_iniziale)])   # Per tenere traccia dei nodi visitati con il relativo stato dello stomaco
                                                        # NB!! Utilizzo un set per evitare di memorizzare i nodi già visitati
                                                                                                            
    # NB!! Per tenere traccia del percorso, memorizzo il padre dei nodi che vado a visitare 
    parent = {(nodo_sorgente, stato_iniziale): None}    
    while q:
        nodo, stato_stomaco = q.popleft()   # Estraggo il primo nodo dalla coda -> al 1° giro sarà il nodo 0
        # Controllo se stiamo tornando al nodo di partenza con lo stato dello stomaco a 1 (SLURP)
        if nodo == nodo_sorgente and stato_stomaco == 1:
            # Se il nodo estratto dalla coda è il nodo di partenza e Tecla si trova nello stato SLURP, allora ricostruisco il percorso 
            percorso = []
            nodo_corrente = (nodo, stato_stomaco)
            while nodo_corrente is not None:
                nodo, stato_stomaco = nodo_corrente
                percorso.append(nodo)
                nodo_corrente = parent[nodo_corrente]
            percorso.reverse()
            return len(percorso) - 1, percorso
        # Altrimenti esploro i nodi adiancenti
        for adiacente in grafo[nodo]:
            nuovo_stato = 1 - stato_stomaco
            if (adiacente, nuovo_stato) not in visitati:
                visitati.add((adiacente, nuovo_stato))
                parent[(adiacente, nuovo_stato)] = (nodo, stato_stomaco)
                q.append((adiacente, nuovo_stato))
    
    return 0, [0]  # In caso non ci sia un percorso valido

# Lettura dell'input
T = int(input())  # Numero di test case
for _ in range(T):
    n, m = map(int, input().split())  # Leggo il numero di nodi (n) e il numero di archi (m)
    grafo = defaultdict(list)  # Andiamo a creare il grafo
    for __ in range(m):  # Cicliamo sul numero di archi
        u, v = map(int, input().split())
        grafo[u].append(v)  # Aggiungo l'arco che vi è tra la coppia di nodi u-v
        grafo[v].append(u)  # NB!! Ho inserito l'arco da entrambe le direzioni, perchè il grafo non è diretto
    spostamenti, percorso = from_zero_to_zero(grafo, 0, n)
    print(spostamenti)
    print(" ".join(map(str, percorso)))
