import time
import random
from naive_string_matching import NaiveStringMatching
from KnuthMorrisPratt import KnuthMorrisPratt

class ExperimentRunner:

    def __init__(self):
        pass

    def execute_naive(self, text, pattern):
        matcher = NaiveStringMatching(text, pattern)
        start_time = time.time()
        result = matcher.find_pattern()
        elapsed_time = time.time() - start_time
        return elapsed_time
    
    def execute_kmp(self, text, pattern):
        matcher = KnuthMorrisPratt(pattern)
        start_time = time.time()
        result = matcher.search(text)
        elapsed_time = time.time() - start_time
        return elapsed_time
    
    def generate_random_string(self,length, charset = "abcdefghijklmnopqrstuvwxyz"):
        return ''.join(random.choice(charset) for _ in range(length))
    
    def run_experiments(self):
        results = []

        # Test 1: Testo casuale e pattern casuale con dimensioni crescenti
        for size in [100, 1000, 10000]:
            text = self.generate_random_string(size)
            pattern = self.generate_random_string(size // 2)
            naive_time = self.execute_naive(text, pattern)
            kmp_time = self.execute_kmp(text, pattern)
            results.append({'test': 'Testo casuale e Pattern casuale', 'size': size, 'naive_time': naive_time, 'kmp_time': kmp_time})

        # Test 2: Testo lungo e pattern breve
        for size in [1000, 10000, 50000]:
            text = self.generate_random_string(size)
            pattern = self.generate_random_string(5)
            naive_time = self.execute_naive(text, pattern)
            kmp_time = self.execute_kmp(text, pattern)
            results.append({'test': 'Testo lungo e Pattern breve', 'size': size, 'naive_time': naive_time, 'kmp_time': kmp_time})

        # Test 3: Testo ripetitivo con un pattern lungo
        for size in [100, 1000, 10000]:
            text = "a" * size
            pattern = "a" * (size // 2)
            naive_time = self.execute_naive(text, pattern)
            kmp_time = self.execute_kmp(text, pattern)
            results.append({'test': 'Testo ripetitivo e Pattern lungo', 'size': size, 'naive_time': naive_time, 'kmp_time': kmp_time})

        # Test 4: Pattern non presente nel testo
        for size in [100, 1000, 10000]:
            text = self.generate_random_string(size, charset="abc")
            pattern = self.generate_random_string(10, charset="xyz")
            naive_time = self.execute_naive(text, pattern)
            kmp_time = self.execute_kmp(text, pattern)
            results.append({'test': 'Pattern non presente', 'size': size, 'naive_time': naive_time, 'kmp_time': kmp_time})
        return results

    def display_results(self, results):
        print("\nRisultati degli esperimenti\n")
        print(f"{'Test':<30}{'Dimensione':<10}{'Tempo Naive (s)':<20}{'Tempo KMP (s)':<20}")
        print("=" * 80)
        for result in results:
            test = result['test']
            size = result['size']
            naive_time = result['naive_time']
            kmp_time = result['kmp_time']
            print(f"{test:<30}{size:<10}{naive_time:<20.6f}{kmp_time:<20.6f}")
        print("\n")