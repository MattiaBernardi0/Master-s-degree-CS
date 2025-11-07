#!/usr/bin/python3
import bisect

def massima_sottosequenza(n, sequenza):
    # NB!! La LIS deve iniziare con il 1° elemento della sequenza presa in input. Questo ha come conseguenza che:
    #   - Tutti i numeri più piccoli del 1° elemento non devono essere presi in considerazione
    
    indici_lis = [0]    # Dato che il 1° numero viene sempre preso
    sequenza_temporanea_crescente = [sequenza[0]]
    posizioni = [-1] * n    # Tiene traccia della posizione di ciascun elemento della LIS ed inzialmente nessun numero è stato posizionato
    posizioni[0] = 0
    predecessore = [-1] * n # Lista per memorizzare il predecessore di ogni elemento della LIS ed inizialmente non ci sono predecessori assegnati
    
    for i in range(1, n):
        if sequenza[i] > sequenza[0]:   # Considero solamente i numeri maggiori del 1° numero 
            if sequenza[i] > sequenza_temporanea_crescente[-1]: # Controllo se l'elemento corrente è maggiore dell'ultimo elemento della 'sequenza_temporanea_crescente'
                predecessore[i] = indici_lis[-1]    # Aggiorno il predecessore dell'elemento corrente all'ultimo indice della 'lis_indices'
                sequenza_temporanea_crescente.append(sequenza[i])   
                posizioni[i] = len(sequenza_temporanea_crescente) - 1   # Aggiorno la posizione dell'elemento corrente
                indici_lis.append(i)
            else:   # Se l'elemento corrente non è maggiore dell'ultimo elemento della 'equenza_temporanea_crescente', cerchiamo la posizione corretta in cui inserirlo per mantenere l'ordine crescente
                posizione = bisect.bisect_left(sequenza_temporanea_crescente, sequenza[i])
                sequenza_temporanea_crescente[posizione] = sequenza[i]  # Sostituiamo l'elemento nella posizione trovata
                posizioni[i] = posizione    # Aggiorno la posizione 
                if posizione > 0:   
                    predecessore[i] = indici_lis[posizione - 1] # Se la posizione è maggiore di 0, allora l'elemento corrente ha un predecessore
                indici_lis[posizione] = i   
            
    # Ricostruiamo gli indici della LIS partendo dal primo elemento
    lunghezza_lis = len(sequenza_temporanea_crescente)
    indici_lis = []
    indice_corrente = posizioni.index(lunghezza_lis - 1)
    
    while indice_corrente != -1:
        indici_lis.append(indice_corrente)
        indice_corrente = predecessore[indice_corrente]
        
    indici_lis.reverse()
    
    # Calcolo dei punti soddisfazione -> se nella LIS non ci sono due indici consecutivi, allora i punti soddisfazioni sono uguali alla lunghezza della LIS, 
    # mentre se ci sono indici consecutivi (come per esempio: 0, 1) allora i punti soddisfazione sono: len(LIS) - 1 
    punti_soddisfazione = lunghezza_lis
    for i in range(len(indici_lis) - 1):
        if indici_lis[i + 1] == indici_lis[i] + 1:
            punti_soddisfazione -= 1
    return indici_lis, lunghezza_lis, punti_soddisfazione
    
T = int(input())    # Numero di test case
for _ in range(T):
    n = int(input())    # Lunghezza della sequenza
    sequenza = list(map(int, input().split()))
    
    indici_panini, panini_mangiati, punti_soddisfazione = massima_sottosequenza(n, sequenza)
    
    print(panini_mangiati, punti_soddisfazione)
    print(" ".join(map(str, indici_panini)))