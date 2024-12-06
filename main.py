import time
from KnuthMorrisPratt import KnuthMorrisPratt
from naive_string_matching import NaiveStringMatching

# CASI DI TEST
test_cases = [
    {"text": "a" * 1000 + "b", "pattern": "a" * 500 + "b"},
    {"text": "abc" * 100, "pattern": "abcabc"},
    {"text": "abacababacab" * 10, "pattern": "abacab"},
    {"text": "aaaaaa", "pattern": "aaa"},
    {"text": "hello world", "pattern": "test"},
    # Casi complessi per verificare le prestazioni
    {"text": "a" * 100000, "pattern": "a" * 50000},
    {"text": "abababababababababababababababababababababababababababababababababababab", "pattern": "abababababababababababab"},
    {"text": "a" * 1000 + "b" * 1000, "pattern": "ab" * 500},
]

# ESECUZIONE DEGLI ALGORITMI
def execute_naive(text, pattern):
    matcher = NaiveStringMatching(text, pattern)
    start_time = time.time()
    result = matcher.find_pattern()
    elapsed_time = time.time() - start_time
    print(f"Naive - Tempo misurato: {elapsed_time:.6f}s")  # DEBUG
    return result, elapsed_time

def execute_kmp(text, pattern):
    matcher = KnuthMorrisPratt(pattern)
    start_time = time.time()
    result = matcher.search(text)
    elapsed_time = time.time() - start_time
    print(f"KMP - Tempo misurato: {elapsed_time:.6f}s")  # DEBUG
    return result, elapsed_time

# CONFRONTO DEI RISULTATI
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
        # Confronta i risultati
        if naive_result != kmp_result:
            print(f"⚠️ Discrepanza nei risultati: Naive={naive_result}, KMP={kmp_result}")
        else:
            print(f"✔️ Risultati coincidenti.")
        # Stampa i tempi
        print(f"Naive: {naive_time:.6f}s, KMP: {kmp_time:.6f}s")
        print("-" * 40)

# PROGRAMMA PRINCIPALE
if __name__ == "__main__":
    print("\n###########################")
    print("# PROGRAMMA STRING MATCHING #")
    print("###########################\n")
    run_tests()
    print("FINE")
