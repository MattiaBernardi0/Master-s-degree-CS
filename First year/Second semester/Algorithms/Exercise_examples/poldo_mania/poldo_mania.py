#!/usr/bin/python3
import bisect

def massima_sottosequenza(n, sequenza):
    lis = [1] * n   # La inizializzo a 1, perchè posso sempre mangiare il panino disponibile
    sequenza_temporanea_crescente = []    # Lista per mantenere la sequenza crescente temporale 
    
    for i in range(n):  # Parto dal sx e scorro verso dx e trovo le massime sotto-sequenze crescenti
        posizione = bisect.bisect_left(sequenza_temporanea_crescente, sequenza[i])    # Trovo la corretta posizione (per mantenere l'ordine) nella lista 'sequenza_temporanea' in cui andare ad inserire
                                                                                        # sequenza[i], utilizzando la ricerca binaria
        if posizione < len(sequenza_temporanea_crescente):
            sequenza_temporanea_crescente[posizione] = sequenza[i]
        else:
            sequenza_temporanea_crescente.append(sequenza[i])
        lis[i] = posizione + 1

    # Adesso faccio la stessa cosa, solamente che scorro la sequenza iniziale da dx a sx e trovo le massime sotto-sequenze decrescenti
    lds = [1] * n   # La inizializzo sempre a 1, perchè posso sempre mangiare il panino disponibile
    sequenza_temporanea_decrescente = []
    
    for i in range(n - 1, -1, -1):  # Parto da dx e vado a sx
        posizione = bisect.bisect_left(sequenza_temporanea_decrescente, -sequenza[i])
        if posizione < len(sequenza_temporanea_decrescente):
            sequenza_temporanea_decrescente[posizione] = -sequenza[i]
        else:
            sequenza_temporanea_decrescente.append(-sequenza[i])
        lds[i] = posizione + 1
    
    #Una volta che ho calcolato le massime sotto-sequenze, l'idea è di sommare lis[i] + lds[i] - 1
    sottosequenza_massima = [0] * n    # Lista per memorizzare tutte la lunghezza delle massime sotto-sequenze
    for i in range(n):
        sottosequenza_massima[i] = lis[i] + lds[i] - 1
    
    return sottosequenza_massima

# Lettura dell'input
T = int(input())  # Numero di testcase
risultato = []  # Lista per contenere le sotto-sequenze massime che includono l'elemento

for _ in range(T):
    n = int(input())  # Lunghezza della sequenza
    sequenza = list(map(int, input().split()))  # Sequenza di numeri interi
    risultato = massima_sottosequenza(n, sequenza)
    print(" ".join(map(str, risultato)))