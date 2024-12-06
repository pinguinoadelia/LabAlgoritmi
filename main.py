import time
import os
import sys

from naive_string_matching import NaiveStringMatching
from KnuthMorrisPratt import KnuthMorrisPratt

#Imposta il limite di ricorsione per evitare problemi con input molto grandi
sys.setrecursionlimit(10000)

#Definizione dei casi di test

test_cases = [
 {"text": "a" * 1000 + "b", "pattern": "a" * 500 + "b"},
 {"text": "abc" * 100, "pattern": "abacab"},
 {"text": "abacababacab" * 10, "pattern": "abacab"},
 {"text": "aaaaaa", "pattern": "aaa"},
 {"text": "hello world", "pattern": "test"}
]

#Definizione delle funzioni

def execute_naive(text: str, pattern: str):
    """
    Esegue l'algoritmo di String Matching Ingenuo.
    Restituisce le posizioni delle occorrenze e il tempo di esecuzione in secondi.
    """
    matcher = NaiveStringMatching(text, pattern)
    start_time = time.time()
    result = matcher.find_pattern()
    elapsed_time = time.time() - start_time
    return result, elapsed_time

def execute_KMP(text: str, pattern:str):
    """
    Esegue l'algoritmo Knuth-Morris-Pratt (KMP).
    Restituisce le posizioni delle occorrenze e il tempo di esecuzione in secondi.
    """
    matcher = KnuthMorrisPratt(pattern)
    start_time = time.time()
    result = matcher.search(text)
    elapsed_time = time.time() - start_time
    return result, elapsed_time

def run_tests(test_cases:list):
    """
    Esegue una serie di test per confrontare gli algoritmi Ingenuo e KMP.
    Stampa i risultati e i tempi di esecuzione per ogni caso di test.
    """
    print("Esecuzione dei test:")
    for i, test in enumerate(test_cases, 1):
        text = test["text"]
        pattern = test["pattern"]
        print(f"\nTest {i}/{len(test_cases)} ({round(i/len(test_cases) * 100, 2)}%): ")
        print(f"Testo: lunghezza{len(text)}, Pattern: lunghezza{len(pattern)}")

        #String Matching ingenuo
        naive_result, naive_time = execute_naive(text, pattern)
        print(f"Ingenuo - Posizioni: {naive_result}, Tempo: {naive_time:.6f} s")

        #Knuth-Morris-Pratt (KMP)
        kmp_result, kmp_time = execute_KMP(text, pattern)
        print(f"KMP - Posizioni: {kmp_result}, Tempo: {kmp_time:.6f} s")

# Programma principale

if __name__ == "__main__":
    # --------------------------------------------------------------------------------------------------------------
    print("\n###########################")
    print("# PROGRAMMA STRING MATCHING #")
    print("###########################\n")

    #Esecuzione dei test

    run_tests(test_cases)

    # --------------------------------------------------------------------------------------------------------------

    print("FINE")

