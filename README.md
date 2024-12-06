# LabAlgoritmi

String Matching Algorithms:

Questo progetto offre un'implementazione completa e una comparazione tra due algoritmi fondamentali per la ricerca di pattern in stringhe: l'algoritmo ingenuo (Naive String Matching) e l'algoritmo di Knuth-Morris-Pratt (KMP). L'obiettivo è fornire una comprensione approfondita dei principi, delle prestazioni e delle applicazioni pratiche di questi metodi.

Introduzione agli Algoritmi:

- Algoritmo Ingenuo (Naive String Matching):
L'algoritmo ingenuo rappresenta il metodo più semplice per cercare un pattern in un testo. Esamina ogni possibile allineamento del pattern con il testo e verifica se i caratteri coincidono. Non utilizza alcuna conoscenza aggiuntiva sulla struttura del pattern o del testo.

Caratteristiche principali:

1. Approccio basato su una scansione diretta.

2. Inefficiente nei casi peggiori, specialmente quando il pattern presenta ripetizioni o corrispondenze parziali frequenti.

Complessità computazionale:

1. Caso peggiore: 𝑂((𝑛 − 𝑚 + 1)⋅𝑚) (per esempio se ci fosse un pattern "aaa", in un testo "aaaaaaaaa")

2. Caso migliore: 𝑂((𝑛 − 𝑚 + 1)⋅𝑚) (non ottimizzato per alcuna situazione)

Implementazione:

L'algoritmo è implementato nella classe NaiveStringMatching. Le principali funzioni offerte includono:

1. find_pattern(): Restituisce le posizioni in cui il pattern si verifica nel testo.

2. display_matches(): Stampa a schermo le posizioni delle occorrenze trovate.

- Algoritmo di Knuth-Morris-Pratt (KMP)
Il KMP è un algoritmo ottimizzato che evita di riesaminare parti del testo già confrontate con successo. Utilizza una funzione prefisso (π) che consente di sapere quanto si può "spostare" il pattern senza perdere informazioni utili.

Caratteristiche principali:

1. Efficace su pattern con ripetizioni e grandi dataset.

2. Utilizza un'analisi preliminare del pattern (π) per ridurre la ridondanza durante il matching.

Complessità computazionale:

1. Pre-elaborazione: 𝑂(𝑚) per calcolare la funzione prefisso.

2. Matching: 𝑂(𝑛), indipendentemente dalla complessità del pattern.

Implementazione:
La classe KnuthMorrisPratt implementa le seguenti funzioni:

compute_prefix_function(): Calcola la funzione prefisso per il pattern.

search(): Esegue il pattern matching e restituisce le posizioni delle occorrenze.

print_prefix_function(): Mostra la funzione prefisso calcolata.

Confronto Pratico tra Naive String Matching e Knuth-Morris-Pratt (KMP):

I due algoritmi differiscono significativamente sia in termini di prestazioni che di struttura. Di seguito, vengono evidenziate le principali differenze:

1. Complessità Pre-elaborazione:

- L'algoritmo ingenuo non richiede alcuna pre-elaborazione del pattern; si limita a confrontare direttamente il pattern con il testo.

- L'algoritmo KMP, invece, pre-elabora il pattern calcolando una funzione prefisso (π), il che richiede un tempo di 𝑂(𝑚), dove 𝑚 è la lunghezza del pattern.

2. Complessità del Matching:

- L'algoritmo ingenuo ha una complessità di matching 𝑂((𝑛 − 𝑚 + 1)⋅𝑚),dove n è la lunghezza del testo. Nei casi peggiori, può risultare molto lento, ad esempio quando il pattern contiene molte ripetizioni.

- L'algoritmo KMP riduce la complessità del matching a 𝑂(𝑛), indipendentemente dalla struttura del pattern, rendendolo estremamente efficiente anche per testi di grandi dimensioni.

3. Efficienza:

- L'approccio ingenuo può essere accettabile per testi brevi o quando non ci sono ripetizioni significative nel pattern, ma diventa inefficiente per pattern complessi o testi molto lunghi.

- L'algoritmo KMP è altamente ottimizzato per tutti i tipi di pattern e si adatta bene a scenari con dataset di grandi dimensioni o ripetizioni frequenti.

4. Memoria Aggiuntiva:

- L'algoritmo ingenuo non utilizza memoria aggiuntiva significativa.

- L'algoritmo KMP richiede un array aggiuntivo (π) per memorizzare la funzione prefisso del pattern, ma l'overhead è minimo.

5. Facilità di Implementazione:

- L'algoritmo ingenuo è estremamente semplice da implementare, con un approccio diretto e lineare.

- L'algoritmo KMP richiede una comprensione più approfondita della funzione prefisso e una logica più complessa per la gestione del matching, risultando moderatamente più difficile da implementare.