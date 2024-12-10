import time
import matplotlib.pyplot as plt
import pandas as pd
from naive_string_matching import NaiveStringMatching
from KnuthMorrisPratt import KnuthMorrisPratt
from experiment_runner import ExperimentRunner

# CASI DI TEST
test_cases = [
    {"text": "a" * 1000 + "b", "pattern": "a" * 500 + "b"},
    {"text": "abc" * 100, "pattern": "abcabc"},
    {"text": "abacababacab" * 10, "pattern": "abacab"},
    {"text": "aaaaaa", "pattern": "aaa"},
    {"text": "hello world", "pattern": "test"},
    {"text": "a" * 100000, "pattern": "a" * 50000},
    {"text": "abababababababababababababababababababababababababababababababababababab", "pattern": "abababababababababababab"},
    {"text": "a" * 1000 + "b" * 1000, "pattern": "ab" * 500},
    {"text": "abcdefgh", "pattern": "xyz"},  
    {"text": "aaaaaa", "pattern": "a"},     
    {"text": "a", "pattern": "aaaa"},       
    {"text": "short", "pattern": "sh"},     
    {"text": "abababababababababababababababababababababababababababababababababababab", "pattern": "abababab"},
    {"text": "a" * 500000, "pattern": "a" * 250000}, 
    {"text": "abcabcabcabcabcabcabcabcabcabcabc", "pattern": "abcabcabcabc"},  
    {"text": "a" * 100000 + "b" * 100000, "pattern": "a" * 50000 + "b" * 50000}  
]

# ESECUZIONE DEGLI ALGORITMI
def execute_naive(text, pattern):
    matcher = NaiveStringMatching(text, pattern)
    start_time = time.time()
    result = matcher.find_pattern()
    elapsed_time = time.time() - start_time
    return result, elapsed_time

def execute_kmp(text, pattern):
    matcher = KnuthMorrisPratt(pattern)
    start_time = time.time()
    result = matcher.search(text)
    elapsed_time = time.time() - start_time
    return result, elapsed_time

# ESECUZIONE DEI TEST
def run_tests():
    print("Esecuzione dei test...\n")
    results = []  # Per raccogliere i dati per i grafici
    for i, test in enumerate(test_cases, 1):
        text = test["text"]
        pattern = test["pattern"]
        print(f"Test {i}/{len(test_cases)}:")
        print(f"Testo: lunghezza {len(text)}, Pattern: lunghezza {len(pattern)}")
        
        # Esegui il Naive
        naive_result, naive_time = execute_naive(text, pattern)
        
        # Esegui il KMP
        kmp_result, kmp_time = execute_kmp(text, pattern)

        # Ordina i risultati
        naive_result = sorted(naive_result)
        kmp_result = sorted(kmp_result)

        # Mostra i risultati ottenuti da entrambi gli algoritmi
        print(f"Naive trova {len(naive_result)} occorrenze: {naive_result[:5]}...")  # Mostra solo i primi 5
        print(f"KMP trova {len(kmp_result)} occorrenze: {kmp_result[:5]}...")  # Mostra solo i primi 5
        
        # Stampa i tempi
        print(f"Tempo Naive: {naive_time:.6f}s")
        print(f"Tempo KMP: {kmp_time:.6f}s")
        print("-" * 40)

        # Salva i dati per la visualizzazione dei grafici
        results.append({
            'test_index': i,
            'text_length': len(text),
            'pattern_length': len(pattern),
            'naive_time': naive_time,
            'kmp_time': kmp_time
        })
    
    # Converti i risultati in DataFrame per una migliore visualizzazione
    df = pd.DataFrame(results)

    # Visualizzazione della tabella dei risultati
    print("\nTest Results:\n", df)

    # Generazione e visualizzazione dei grafici
    plt.figure(figsize=(10, 6))
    plt.plot(df['test_index'], df['naive_time'], marker='o', label='Naive Algorithm')
    plt.plot(df['test_index'], df['kmp_time'], marker='o', label='KMP Algorithm')
    plt.xlabel('Indice del Test')
    plt.ylabel('Tempo di esecuzione (secondi)')
    plt.title('Confronto dei tempi di esecuzione per ciascun test')
    plt.xticks(df['test_index'])
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()


# ESECUZIONE DEGLI ESPERIMENTI
def run_experiments():
    """Esegue una serie di esperimenti volti a confrontare gli algoritmi Naive e KMP."""
    runner = ExperimentRunner()
    print("\nEsecuzione degli esperimenti per confrontare le prestazioni degli algoritmi...\n")
    experiment_results = runner.run_experiments()
    runner.display_results(experiment_results)
    df = pd.DataFrame(experiment_results)

    # Visualizzazione della tabella dei risultati
    print("\nTest Results:\n", df)

    # Generazione e visualizzazione dei grafici
    for test_name in df['test'].unique():
        subset = df[df['test'] == test_name]
        plt.figure(figsize=(10, 6))
        plt.plot(subset['size'], subset['naive_time'], marker='o', label='Naive Algorithm')
        plt.plot(subset['size'], subset['kmp_time'], marker='o', label='KMP Algorithm')
        plt.xlabel('Dimensione del testo')
        plt.ylabel('Tempo di esecuzione (secondi)')
        plt.title(f'Confronto dei tempi di esecuzione per {test_name}')
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.show()

# PROGRAMMA PRINCIPALE
if __name__ == "__main__":
    print("\n###########################")
    print("# PROGRAMMA STRING MATCHING #")
    print("###########################\n")
    run_tests()
    run_experiments()
    print("FINE")
