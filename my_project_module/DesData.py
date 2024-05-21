import numpy as np
from stat_tables import StatTables

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

    def ml_bound(self, confidence_level):
        avg = self.mean()
        std_dev = self.samp_dev()
        n = len(self.data)

        if n > 30:
            z = StatTables.get_z_value(confidence_level)
            return avg - (z * (std_dev / np.sqrt(n)))
        else:
            t = StatTables.get_t_value(confidence_level, n - 1)
            return avg - (t * (std_dev / np.sqrt(n)))

    def ml_bound_with_sigma(self, confidence_level, sigma):
        avg = self.mean()
        n = len(self.data)

        if n > 30:
            z = StatTables.get_z_value(confidence_level)
            return avg - (z * (sigma / np.sqrt(n)))
        else:
            t = StatTables.get_t_value(confidence_level, n - 1)
            return avg - (t * (sigma / np.sqrt(n)))

    def ml_bound_full(self, confidence_level, sigma, mean, sample):
        if sample > 30:
            z = StatTables.get_z_value(confidence_level)
            return mean - (z * (sigma / np.sqrt(sample)))
        else:
            t = StatTables.get_t_value(confidence_level, sample - 1)
            return mean - (t * (sigma / np.sqrt(sample)))

    def mu_bound(self, confidence_level):
        avg = self.mean()
        std_dev = self.samp_dev()
        n = len(self.data)

        if n > 30:
            z = StatTables.get_z_value(confidence_level)
            return avg + (z * (std_dev / np.sqrt(n)))
        else:
            t = StatTables.get_t_value(confidence_level, n - 1)
            return avg + (t * (std_dev / np.sqrt(n)))

    def mu_bound_with_sigma(self, confidence_level, sigma):
        avg = self.mean()
        n = len(self.data)

        if n > 30:
            z = StatTables.get_z_value(confidence_level)
            return avg + (z * (sigma / np.sqrt(n)))
        else:
            t = StatTables.get_t_value(confidence_level, n - 1)
            return avg + (t * (sigma / np.sqrt(n)))

    def mu_bound_full(self, confidence_level, sigma, mean, sample):
        if sample > 30:
            z = StatTables.get_z_value(confidence_level)
            return mean + (z * (sigma / np.sqrt(sample)))
        else:
            t = StatTables.get_t_value(confidence_level, sample - 1)
            return mean + (t * (sigma / np.sqrt(sample)))

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
