import numpy as np
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.append(current_dir)

from StatTables import StatTables

class DesData:
    def __init__(self, data=None):
        self.data = np.array(data) if data is not None else np.array([])

    def mean(self):
        return np.mean(self.data)

    def vari(self):
        return np.var(self.data)

    def dev(self):
        return np.std(self.data)

    def samp_vari(self):
        return np.var(self.data, ddof=1)

    def samp_dev(self):
        return np.std(self.data, ddof=1)

    def median(self):
        return np.median(self.data)

    def mode(self):
        values, counts = np.unique(self.data, return_counts=True)
        max_count_index = np.argmax(counts)
        if np.sum(counts == counts[max_count_index]) > 1:
            return float('nan')  # Multiple modes
        return values[max_count_index]

    def bound(self, confidence_level, sigma=None, mean=None, sample=None, upper=False):
        avg = self.mean() if mean is None else mean
        std_dev = self.samp_dev() if sigma is None else sigma
        n = len(self.data) if sample is None else sample

        if n > 30:
            z = StatTables.get_z_value(confidence_level)
            margin_of_error = z * (std_dev / np.sqrt(n))
        else:
            t = StatTables.get_t_value(confidence_level, n - 1)
            margin_of_error = t * (std_dev / np.sqrt(n))

        return avg + margin_of_error if upper else avg - margin_of_error

    def p_ci(self, confidence_level, successes, trials):
        if trials == 0:
            raise ValueError("Number of trials must be greater than 0")
        if successes > trials:
            raise ValueError("Number of successes cannot exceed number of trials")

        z = StatTables.get_z_value(confidence_level)
        p = successes / trials
        margin_of_error = z * np.sqrt((p * (1 - p)) / trials)

        lower_bound = max(p - margin_of_error, 0)
        upper_bound = p + margin_of_error

        return lower_bound, upper_bound

    def var_ci(self, confidence_level):
        variance = self.samp_vari()
        sample_size = len(self.data)
        if sample_size < 2:
            raise ValueError("Sample size must be greater than 1 for variance estimation.")

        r_chi_value = StatTables.get_r_chi_value(confidence_level, sample_size - 1)
        l_chi_value = StatTables.get_l_chi_value(confidence_level, sample_size - 1)
        lower_bound = (sample_size - 1) * variance / r_chi_value
        upper_bound = (sample_size - 1) * variance / l_chi_value

        return lower_bound, upper_bound

    def var_ci_full(self, confidence_level, variance, sample_size):
        if sample_size < 2:
            raise ValueError("Sample size must be greater than 1 for variance estimation.")

        r_chi_value = StatTables.get_r_chi_value(confidence_level, sample_size - 1)
        l_chi_value = StatTables.get_l_chi_value(confidence_level, sample_size - 1)
        lower_bound = (sample_size - 1) * variance / r_chi_value
        upper_bound = (sample_size - 1) * variance / l_chi_value

        return lower_bound, upper_bound
