#!/usr/bin/python3

#Matricola: VR502842

def resto_minimo(resto, tagli_di_monete):
    numero_pezzi = 0    # Contatore per il numero totale di pezzi utilizzati
    pezzi_utilizzati = [0] * len(tagli_di_monete)   # Lista contenente i tagli di moneta utilizzati

    for taglio_di_moneta in reversed(tagli_di_monete):
        quantita = resto // taglio_di_moneta    # Faccio la divisione intera e il quoziente lo assegno a 'quantita', 
                                                # in modo da vedere quante volte il taglio di moneta (su cui stiamo iterando) può essere sottratto dal resto
        
        pezzi_utilizzati[tagli_di_monete.index(taglio_di_moneta)] = quantita   # Memorizzo il numero di pezzi utilizzati per il taglio corrente, andando a prendere l'indice del taglio corrente
        resto %= taglio_di_moneta   # Calcola il resto rimanente
        numero_pezzi += quantita    # Aggiorna il numero totale di pezzi utilizzati
    
    return numero_pezzi, pezzi_utilizzati

T = int(input())    # Numero di test case
for _ in range(T):
    # Ricevo in input il resto
    resto = int(input())
    assert (resto > 0)  # Per assicurarmi che il resto sia positivo
    
    tagli_di_monete = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]    # Lista contenente i tagli di monete disponibili
    
    # Calcolo il numero minimo di pezzi che utilizzo per dare il resto (numero_pezzi) e i tagli di monete che utilizzo (pezzi_utilizzati)
    numero_pezzi, pezzi_utilizzati = resto_minimo(resto, tagli_di_monete)
    
    # Output
    print(numero_pezzi)  
    print(' '.join(map(str, pezzi_utilizzati)))




