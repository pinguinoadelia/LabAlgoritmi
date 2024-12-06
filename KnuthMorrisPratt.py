from KnuthMorrisPratt import KnuthMorrisPratt

class KnuthMorrisPratt:

    def __init__(self, pattern):
        """
        Inizializza la classe con il pattern e calcola la funzione prefisso.
        """
        self.pattern = pattern    

    def compute_prefix_function(self, pattern):
        """
        Calcola la funzione prefisso per il pattern.
        """
        m = len(pattern)
        pi = [0] * m
        k = 0
        for q in range (1,m):
            while k > 0 and pattern[k] != pattern[q]:
                k = pi[k - 1]
            if pattern[k] == pattern[q]:
                k += 1
            pi[q] = k
        return pi
    
    def search(self, text):
        """
        Esegue il pattern matching sul testo usando il pattern predefinito.
        """
        n = len(text)
        m = len(self.pattern)
        q = 0
        matches = []
        for i in range (n):
            while q > 0 and self.pattern[q] != text[i]:
                q = self.pi[q - i]
            if self.pattern[q] == text[i]:
                q += 1
            if q == m:
                matches.append(i - m + 1)
                q = self.pi[q - 1]
        return matches     

    def print_prefix_function(self):
        """
        Stampa l'array della funzione prefisso.
        """
        print(f"Funzione prefisso (π) per il pattern '{self.pattern}': {self.pi}")

    if __name__ == "__main__":
        """
        Esempio di utilizzo della classe KnuthMorrisPratt per il pattern matching.
         """
        pattern = "ababaca"
        text = "ababcabababaca"
        kmp = KnuthMorrisPratt(pattern)
        kmp.print_prefix_function
        matches = kmp.search(text)
        print(f"Il pattern è stato trovato alle posizioni: {matches}")

    
          







        

