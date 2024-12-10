import time
import random
from naive_string_matching import NaiveStringMatching
from KnuthMorrisPratt import KnuthMorrisPratt

class ExperimentRunner:
     """Classe per eseguire una serie di esperimenti volti ad analizzare 
     le prestazioni degli algoritmi di Naive String Matching e Knuth-Morris-Pratt.
     Questa classe genera i casi di test, esegue gli algoritmi e registra i risultati.
    """

     def __init__(self):
        """Inizializza la classe ExperimentRunner senza parametri."""
        pass

     def execute_naive(self, text, pattern):
        """Esegue l'algoritmo Naive String Matching e misura il tempo di esecuzione.
        
        Args:
            text (str): Il testo in cui verrà cercato il pattern.
            pattern (str): Il pattern da cercare nel testo.
        
        Returns:
            float: Il tempo impiegato per eseguire l'algoritmo.
        """
        matcher = NaiveStringMatching(text, pattern)
        start_time = time.time()
        result = matcher.find_pattern()
        elapsed_time = time.time() - start_time
        return elapsed_time
    
     def execute_kmp(self, text, pattern):
        """Esegue l'algoritmo Knuth-Morris-Pratt e misura il tempo di esecuzione.
        
        Args:
            text (str): Il testo in cui verrà cercato il pattern.
            pattern (str): Il pattern da cercare nel testo.
        
        Returns:
            float: Il tempo impiegato per eseguire l'algoritmo.
        """
        matcher = KnuthMorrisPratt(pattern)
        start_time = time.time()
        result = matcher.search(text)
        elapsed_time = time.time() - start_time
        return elapsed_time
    
     def generate_random_string(self,length, charset = "abcdefghijklmnopqrstuvwxyz"):
        """Genera una stringa casuale di una lunghezza specifica utilizzando il set di caratteri specificato.
        
        Args:
            length (int): La lunghezza della stringa da generare.
            charset (str, opzionale): I caratteri da utilizzare per generare la stringa. Predefinito: lettere minuscole.
        
        Returns:
            str: Una stringa casuale della lunghezza specificata.
        """
        return ''.join(random.choice(charset) for _ in range(length))
    
     def run_experiments(self):
        """Esegue una serie di esperimenti per confrontare gli algoritmi Naive e KMP su diversi casi di test.
        Gli esperimenti includono casi con lunghezze di testo diverse, pattern e contenuti del testo diversi.
        
        Returns:
            list: Una lista di dizionari contenenti i risultati di ogni esperimento.
        """
        results = []
        # Test 1: Testo casuale e pattern casuale con dimensioni crescenti
        for size in [100, 1000, 10000]:
            text = self.generate_random_string(size)
            pattern = self.generate_random_string(size // 2)
            naive_time = self.execute_naive(text, pattern)
            kmp_time = self.execute_kmp(text, pattern)
            results.append({'test': 'Testo casuale e Pattern casuale', 'size': size, 'naive_time': naive_time, 'kmp_time': kmp_time})

        # Test 2: Testo lungo e pattern breve
        for size in [1000, 1000, 10000]:
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
        """Mostra i risultati degli esperimenti in formato tabellare.
        
        Args:
            results (list): I risultati degli esperimenti come lista di dizionari.
        """
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