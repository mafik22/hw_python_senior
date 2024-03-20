import time

def calculate_execution_time(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

def example_function_to_measure_execution_time(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

import unittest

class TestCalculateExecutionTime(unittest.TestCase):
    def test_execution_time_calculation(self):
        execution_time = calculate_execution_time(example_function_to_measure_execution_time, 1000000)
        self.assertGreater(execution_time, 0)

if __name__ == "__main__":
    unittest.main()
