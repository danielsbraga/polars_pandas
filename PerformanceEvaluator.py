import time
import polars as pl
import pandas as pd
from statistics import mean

class PerformanceEvaluator:
    """
    A class to evaluate and compare the performance of functions.
    """
    
    def __init__(self):
        pass

    def evaluate_time(self, func, *args, **kwargs):
        """
        Evaluates the execution time of a function.

        Parameters:
        func (callable): The function to be timed.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.

        Returns:
        result: The result of the function call.
        execution_time (float): The time taken to execute the function in seconds.
        """
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return result, execution_time

    def averaging(self, func, *args, n=10, library_name="", **kwargs):
        """
        Runs the given function multiple times and returns the mean execution time.

        Parameters:
        func (callable): The function to be averaged.
        *args: Positional arguments to pass to the function.
        n (int): Number of times to run the function.
        library_name (str): Name of the library for informative output.
        **kwargs: Keyword arguments to pass to the function.

        Returns:
        mean_execution_time (float): The mean execution time over n runs.
        """
        execution_times = []

        for _ in range(n):
            _, exec_time = self.evaluate_time(func, *args, **kwargs)
            execution_times.append(exec_time)

        mean_execution_time = mean(execution_times)
        print(f"{library_name} mean execution time over {n} runs: {mean_execution_time:.6f} seconds")

        return mean_execution_time

    def compare_execution_times(self, polars_mean_time, pandas_mean_time):
        """
        Compares the execution times of Polars and Pandas operations.

        Parameters:
        polars_mean_time (float): The mean execution time for the Polars operation.
        pandas_mean_time (float): The mean execution time for the Pandas operation.

        Prints:
        The absolute and relative differences in execution times, indicating which library was faster.
        """
        if polars_mean_time < pandas_mean_time:  # Polars is faster
            absolute_difference = pandas_mean_time - polars_mean_time
            relative_difference = (absolute_difference / pandas_mean_time) * 100
            print("Polars Wins!")
            print(f"The execution time for Polars was {absolute_difference:.2f} seconds faster than Pandas.")
            print(f"Relative Difference: {relative_difference:.2f}% faster!")
        else:  # Pandas is faster
            absolute_difference = polars_mean_time - pandas_mean_time
            relative_difference = (absolute_difference / polars_mean_time) * 100
            print("Pandas Wins!")
            print(f"The execution time for Pandas was {absolute_difference:.2f} seconds faster than Polars.")
            print(f"Relative Difference: {relative_difference:.2f}% faster.")