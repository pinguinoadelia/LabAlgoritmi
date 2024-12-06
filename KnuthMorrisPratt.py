
class KnuthMorrisPratt:

    def __init__(self, pattern):
        self.pattern = pattern    

    def compute_prefix_function(self, pattern):
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
        print(f"Funzione prefisso (π) per il pattern '{self.pattern}': {self.pi}")
    
          







        

