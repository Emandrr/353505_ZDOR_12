import input_self
import math
from statistics import median, mode, variance, stdev


class SequenceBase:
    def __init__(self, sequence):
        # Initializes the SequenceAnalyzer with a sequence
        self.sequence = sequence

    def calculate_mean(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            calculating of mean
            """
        return sum(self.sequence) / len(self.sequence)

    def calculate_median(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            calculating of median
            """
        return median(self.sequence)

    def calculate_mode(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            calculating of mode
            """
        return mode(self.sequence)

    def calculate_variance(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            calculating of variance
            """
        return variance(self.sequence)

    def calculate_standard_deviation(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            calculating of standard variance
            """
        return stdev(self.sequence)


class SequenceAdvanced(SequenceBase):
    def __init__(self, x, eps):
        super().__init__([])
        self._eps = eps
        self._x = x

    def taylor_series(self):
        """
            Developer Pavel Zdor
            date: 20.04.2025
            calculating of taylor series
            """
        res = 0
        n = 0
        real_value = self.calculate_real()
        while abs(res-real_value) > self._eps and n < 50:
            res+=(pow(self._x,2*n+1)*(math.factorial(2*n))/((pow(4,n)) * math.factorial(n) * math.factorial(n)*(2*n+1)))
            n += 1
        table_info = [n, res]
        return table_info

    def calculate_real(self):
        return math.asin(self._x)

