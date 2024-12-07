class NaiveStringMatching:

    def __init__(self, text, pattern):
        """
        Inizializza la classe con il testo e il pattern forniti.
        """
        self.text = text
        self.pattern = pattern

    def find_pattern(self):
        """
        Trova tutte le occorrenze del pattern nel testo.
        """
        n = len(self.text)
        m = len(self.pattern)
        results = []
        for s in range(n - m + 1):
            if self.text[s:s + m] == self.pattern:
                results.append(s)
        return results
