from naive_string_matching import NaiveStringMatching

class NaiveStringMatching:

    """
    Classe per l'algoritmo ingenuo di string matching.
    Trova tutte le occorrenze di un pattern in un testo fornito.
    """

    def __init__(self, text:str, pattern:str):

        """
        Inizializza l'istanza con il testo e il pattern forniti.
        param text: Il testo in cui cercare il pattern.
        param pattern: Il pattern da cercare nel testo.
        """

        self.text = text
        self.pattern = pattern

    def find_pattern(self) -> list:

        """
        Trova tutte le occorrenze del pattern nel testo.
        return: Una lista di posizioni (indici) dove il pattern appare nel testo.
        """

        n = len(self.text)
        m = len(self.pattern) 
        results = [] 
        for s in range (n - m + 1):  
            if self.text[s:s + m] == self.pattern:
                results.append(s) 
        return results
    
    def display_matches(self):

        """
        Mostra le posizioni in cui il pattern è stato trovato nel testo.
        """

        matches = self.find_pattern()
        if matches:
            print(f"Il pattern '{self.pattern}' è stato trovato nelle posizioni: {matches}")
        else:
            print(f"Il pattern '{self.pattern}' non è stato trovato nel testo")    

    if __name__ == "__main__": 

        """
        Esempio di utilizzo:
        Inizializza la classe con un testo e un pattern e mostra i risultati del matching.
        """
        text = "acaabc"
        pattern = "aab"
        matcher = NaiveStringMatching(text, pattern) 
        matcher.display_matches()       
    
    @staticmethod
    def run_tests():
        test_cases = [
         {"text": "a" * 1000 + "b", "pattern": "a" * 500 + "b", "expected": [500]},
         {"text": "abc" * 100, "pattern": "abcabc", "expected": [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96]},
         {"text": "abacababacab" * 10, "pattern": "abacab", "expected": [2, 10, 22, 30, 42, 50, 62, 70, 82, 90]},
         {"text": "aaaaaa", "pattern": "aaa", "expected": [0, 1, 2, 3]},
         {"text": "hello world", "pattern": "test", "expected": []},
        ]
        print("\nEsecuzione test:\n")
        for i, test in enumerate(test_cases):
            matcher = NaiveStringMatching(test["text"], test["pattern"])
            result = matcher.find_pattern()
            print(f"Test {i + 1}: ", end = "")
            if result == test["expected"]:
                print("Successo")
            else:
                print("Fallimento")
                print(f" Risultato ottenuto: {result}")
                print(f" Risultato atteso: {test['expected']}")   







    