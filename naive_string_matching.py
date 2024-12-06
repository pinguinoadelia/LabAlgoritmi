
class NaiveStringMatching:

    def __init__(self, text:str, pattern:str):
        self.text = text
        self.pattern = pattern

    def find_pattern(self) -> list:
        n = len(self.text)
        m = len(self.pattern)
        results = []
        for s in range (n - m + 1):
            if self.text[s:s + m] == self.pattern:
                results.append(s)
        return results

    