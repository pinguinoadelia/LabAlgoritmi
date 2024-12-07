import time
import random

class ExperimentRunner:

    def __init__(self):
        pass

    def execute_naive(self, text, pattern):
        matcher = NaiveStringMatching(text, pattern)
        start_time = time.time()
        result = matcher.find_pattern()
        elapsed_time = time.time() - start_time
        return elapsed_time
    