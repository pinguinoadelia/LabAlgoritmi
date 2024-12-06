

class KnuthMorrisPratt:

    def __init__(self, pattern):
        """
        Inizializza la classe con il pattern e calcola la funzione prefisso.
        """
        self.pattern = pattern
        self.pi = self.compute_prefix_function(pattern)  # Calcola e assegna self.pi

    def compute_prefix_function(self, pattern):
        """
        Calcola la funzione prefisso per il pattern.
        """
        m = len(pattern)
        pi = [0] * m  # Array prefisso inizializzato a zero
        k = 0
        for q in range(1, m):
            # Torna indietro nel prefisso in caso di mismatch
            while k > 0 and pattern[k] != pattern[q]:
                k = pi[k - 1]
            if pattern[k] == pattern[q]:
                k += 1
            pi[q] = k  # Assegna il valore calcolato
        return pi

    def search(self, text):
        """
        Esegue il pattern matching sul testo usando il pattern predefinito.
        """
        n = len(text)
        m = len(self.pattern)
        q = 0
        matches = []

        for i in range(n):
            # Gestione del mismatch
            while q > 0 and self.pattern[q] != text[i]:
                q = self.pi[q - 1]  # Torna indietro nel prefisso
            
            # Se c'è una corrispondenza
            if self.pattern[q] == text[i]:
                q += 1
            
            # Se l'intero pattern è stato trovato
            if q == m:
                matches.append(i - m + 1)  # Aggiunge la posizione trovata
                q = self.pi[q - 1]  # Continua la ricerca

        return matches

    def print_prefix_function(self):
        """
        Stampa l'array della funzione prefisso.
        """
        print(f"Funzione prefisso (π) per il pattern '{self.pattern}': {self.pi}")

    @staticmethod
    def run_tests():
        """
        Esegue una serie di test sull'algoritmo Knuth-Morris-Pratt.
        """
        tests = [
            {"pattern": "ababaca", "text": "ababcabababaca", "expected": [6]},
            {"pattern": "abc", "text": "abcabcabc", "expected": [0, 3, 6]},
            {"pattern": "aaa", "text": "aaaaaa", "expected": [0, 1, 2, 3]},
            {"pattern": "a", "text": "bbbb", "expected": []},
            {"pattern": "xyz", "text": "abcdefgh", "expected": []},
            {"pattern": "test", "text": "this is a test text with test cases", "expected": [10, 29]},
        ]
        for i, test in enumerate(tests, 1):
            pattern = test["pattern"]
            text = test["text"]
            expected = test["expected"]
            kmp = KnuthMorrisPratt(pattern)
            result = kmp.search(text)
            print(f"Test {i}: pattern '{pattern}' in testo '{text}'")
            print(f"Risultato ottenuto: {result}")
            print(f"Risultato atteso: {expected}")
            print("Passato" if result == expected else "Fallito")
            print("-" * 40)

    if __name__ == "__main__":
        """
        Esempio di utilizzo della classe KnuthMorrisPratt per il pattern matching.
        """
        pattern = "ababaca"
        text = "ababcabababaca"
        kmp = KnuthMorrisPratt(pattern)
        kmp.print_prefix_function()
        matches = kmp.search(text)
        print(f"Il pattern è stato trovato alle posizioni: {matches}")
        print("\nEsecuzione test\n")
        KnuthMorrisPratt.run_tests()

    
          







        

