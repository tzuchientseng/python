from statitic import DesData  # Import the DesData class
class StatisticsDemo:

    @staticmethod
    def main():
        # Specify the desired confidence level for descriptive statistics
        confidence_level = 0.90  # 90% confidence level

        # Initialize the data
        data = [148, 155, 126, 117, 124, 136, 141, 133, 129, 146]
        # Create an instance of DesData with the data
        descriptive_stats = DesData(data)
        
        # Print basic descriptive statistics
        print("Average:", descriptive_stats.mean())
        print("Variance:", descriptive_stats.vari())
        print("Standard Deviation:", descriptive_stats.dev())
        print("Median:", descriptive_stats.median())
        print("Mode:", descriptive_stats.mode())
        print("\nVariance (sample formula):", descriptive_stats.samp_vari())
        print("Standard Deviation (sample formula):", descriptive_stats.samp_dev())

        print("-----------------Descriptive Statistics (Estimate \u03BC)-----------------")
        # Estimate Mean (Sigma unknown)
        try:
            lower_bound_unknown_sigma = descriptive_stats.bound(confidence_level)
            upper_bound_unknown_sigma = descriptive_stats.bound(confidence_level, upper=True)
            print("The mean (\u03BC) estimate (\u03C3 unknown) {}% Confidence Interval: [{:.2f}, {:.2f}]".format(confidence_level * 100, lower_bound_unknown_sigma, upper_bound_unknown_sigma))
        except ValueError as e:
            print("Error calculating confidence interval with unknown sigma:", e)

        # Estimate Mean (Sigma known)
        sigma = 11.27
        try:
            lower_bound_known_sigma = descriptive_stats.bound(confidence_level, sigma=sigma)
            upper_bound_known_sigma = descriptive_stats.bound(confidence_level, sigma=sigma, upper=True)
            print("The mean (\u03BC) estimate (\u03C3 known) {}% Confidence Interval: [{:.2f}, {:.2f}]".format(confidence_level * 100, lower_bound_known_sigma, upper_bound_known_sigma))
        except ValueError as e:
            print("Error calculating confidence interval with known sigma:", e)

        print("\n-----------------Descriptive Statistics (Estimate p)-----------------")
        # Example data for Bernoulli trials
        successes = 6
        trials = 150
        confidence_level_p = 0.99  # Using a different confidence_level

        try:
            interval = descriptive_stats.p_ci(confidence_level_p, successes, trials)
            # Print the confidence interval using the actual `confidence_level_p`
            print("{:.1f}% confidence interval for Bernoulli parameter p: [{:.3f}, {:.3f}]".format(confidence_level_p * 100, interval[0], interval[1]))
        except ValueError as e:
            print("Error:", e)

        print("\n-----------------Descriptive Statistics (Estimate Sigma)-----------------")
        confidence_level_sigma = 0.98  # e.g., 98% confidence level
        data2 = [113, 106, 102, 104, 112, 115, 103, 109]
        descriptive_stats2 = DesData(data2)
        try:
            ci = descriptive_stats2.var_ci(confidence_level_sigma)
            print("98% Confidence Interval for Variance: [{:.2f}, {:.2f}]".format(ci[0], ci[1]))
        except ValueError as e:
            print(e)

        print("\n-----------------Inferential Statistics-----------------")
        # Create an instance of InferentialStatistics with the data
        # inferential_stats = InferData(data)  # Uncomment if InferData is implemented

if __name__ == "__main__":
    StatisticsDemo.main()

