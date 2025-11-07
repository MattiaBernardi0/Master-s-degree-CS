#!/usr/bin/python3
import sys

def bugiardo_incallito(n, k, indice_sinistro, indice_destro, indice_strumento, strumenti):
    if n == 1:
        print(f"!{indice_sinistro}")    # NB!! Non posso mettere print(f"!1") perchè altrimenti il testcase 2 mi dà la risposta sbagliata
                                        # Per questo motivo, quando vado a fare la chiamata ricorsiva, devo andare a modificare il valore di 'n'
        sys.stdout.flush()
        return
    
    mid = (indice_sinistro + indice_destro) // 2
    print(f"?{mid}")
    sys.stdout.flush()
    response = input().strip()
    
    if strumenti[indice_strumento % k] == True:
            if response == '=':
                print(f"!{mid}")
                sys.stdout.flush()
                return
            elif response == '<':
                indice_destro = mid - 1
                bugiardo_incallito(mid - indice_sinistro, k, indice_sinistro, indice_destro, indice_strumento + 1, strumenti)    # Ci richiamiamo in maniera ricorsiva, con l'indice dx modificato
            else:
                indice_sinistro = mid + 1
                bugiardo_incallito(indice_destro - mid, k, indice_sinistro, indice_destro, indice_strumento + 1, strumenti)    # Stessa cosa, solamente che in questo caso cambiamo l'indice sx
                
    else:   # Strumento == False -> abbiamo le risposte invertite rispetto a sopra
        if response == '=':
            print(f"!{mid}")
            sys.stdout.flush()
            return
        elif response == '>':
            indice_destro = mid - 1
            bugiardo_incallito(mid - indice_sinistro, k, indice_sinistro, indice_destro, indice_strumento + 1, strumenti)
        else:
            indice_sinistro = mid + 1
            bugiardo_incallito(indice_destro - mid, k, indice_sinistro, indice_destro, indice_strumento + 1, strumenti)
    

def ricerca_binaria(n, k, b, indice_sinistro, indice_destro):
    # 1° Test case -> n = 1 e di conseguenza il server fornisce subito la risposta corretta
    if n == 1:
        print(f"!{indice_sinistro}")
        sys.stdout.flush()
        return
   
    # Se n != 1, allora dobbiamo utilizzare la ricerca binaria per arrivare ad una soluzione 
    mid = (indice_sinistro + indice_destro) // 2
    
    if b == 0:  # Siamo nel caso ottimo, in cui tutti gli strumenti dicono il vero
        print(f"?{mid}")
        sys.stdout.flush()
        response = input().strip()  # Leggo la risposta inviata dal server
        # Possiamo trovarci in 3 casi: 
        #   1. =    -> quinid abbiamo trovato la soluzione
        #   2. <    -> restingiamo l'intervallo di ricerca a sx
        #   3. >    -> restringiamo l'intervallo a dx
            
        if response == '=':
            print(f"!{mid}")
            sys.stdout.flush()
            return
        elif response == '<':
            indice_destro = mid - 1
            ricerca_binaria(mid - indice_sinistro, k, b, indice_sinistro, indice_destro)    # Ci richiamiamo in maniera ricorsiva, con l'indice dx modificato
        else:
            indice_sinistro = mid + 1
            ricerca_binaria(indice_destro - mid, k, b, indice_sinistro, indice_destro)    # Stessa cosa, solamente che in questo caso cambiamo l'indice sx
         
    else:   # b == 1 -> in questo caso tutti gli strumenti potrebbero dire sempre la verità oppure mentire sempre
        strumenti = [True] * k
        for i in range(k):
            print(f"?{n - i}")
            sys.stdout.flush()
            response = input().strip()
                
            if response == '=':
                print(f"!{n - i}")
                sys.stdout.flush()
                return
            elif response == '>':
                strumenti[i % k] = False
        
        bugiardo_incallito(n - i - 1, k, 1, n - i - 1, 0, strumenti)
        
                      
T = int(input())
for _ in range(T):
    n, k, b = map(int, input().strip().split()) 
    # b = 0 -> tutti gli strumenti dicono il vero
    # b = 1 -> ogni strumenti potrebbe dire sempre il vero OPPURE essere un mentitore seriale (rispondono correttamente solo quando gli si chiede x = x)
    
    # OSSERVAZIONI: vogliamo trovare un numero compreso nell'intervallo [1, n] -> l'idea quindi è di utilizzare la ricerca binaria
    indice_sinistro = 1
    indice_destro = n
    indice_strumento = 0
    
    ricerca_binaria(n, k, b, indice_sinistro, indice_destro)