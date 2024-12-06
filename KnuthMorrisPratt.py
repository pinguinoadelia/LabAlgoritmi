
class KnuthMorrisPratt:

    def __init__(self, pattern):
        this.pattern = pattern    

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
    
          







        

