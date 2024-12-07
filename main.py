import time
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

#Esecuzione degli esperimenti
def run_experiments():
    """Esegue una serie di esperimenti volti a confrontare gli algoritmi Naive e KMP."""
    runner = ExperimentRunner()
    print("\nEsecuzione degli esperimenti per confrontare le prestazioni degli algoritmi...\n")
    experiment_results = runner.run_experiments()
    runner.display_results(experiment_results)

# PROGRAMMA PRINCIPALE
if __name__ == "__main__":
    print("\n###########################")
    print("# PROGRAMMA STRING MATCHING #")
    print("###########################\n")
    run_tests()
    run_experiments()
    print("FINE")

