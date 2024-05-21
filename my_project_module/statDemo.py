from DesData import DesData

class StatisticsDemo:

    @staticmethod
    def main():
        # Specify the desired confidence level for descriptive statistics
        confidence_level = 90  # e.g., 95 for 95% confidence level

        # Initialize the data
        data = [148, 155, 126, 117, 124, 136, 141, 133, 129, 146]
        # Create an instance of DescriptiveStatistics with the data
        descriptive_stats = DesData(data)
        print("Average:", descriptive_stats.mean())
        print("Variance:", descriptive_stats.vari())
        print("Standard Deviation:", descriptive_stats.dev())
        print("Median:", descriptive_stats.median())
        print("Mode:", descriptive_stats.mode())
        print("\nVariance (sample formula):", descriptive_stats.samp_vari())
        print("Standard Deviation (sample formula):", descriptive_stats.samp_dev())

        print("-----------------Descriptive Statistics (Estimate \u03BC)-----------------")
        # Estimate Mean (Sigma unknown)
        print("The mean (\u03BC) estimate (\u03C3 unknown) {}% Confidence Interval: [{}, {}]".format(
            confidence_level, descriptive_stats.ml_bound(confidence_level), descriptive_stats.mu_bound(confidence_level)
        ))
        
        # Estimate Mean (Sigma known)
        sigma = 11.27
        print("The mean (\u03BC) estimate (\u03C3 known) {}% Confidence Interval: [{}, {}]".format(
            confidence_level, descriptive_stats.ml_bound_with_sigma(confidence_level, sigma), descriptive_stats.mu_bound_with_sigma(confidence_level, sigma)
        ))

        print("\n-----------------Descriptive Statistics (Estimate p)-----------------")
        # Example data for Bernoulli trials
        successes = 6
        trials = 150
        confidence_level = 99.0

        try:
            # Assuming descriptiveStats.pCI() returns a double array with the lower and upper bounds of the confidence interval
            interval = descriptive_stats.p_ci(confidence_level, successes, trials)

            # Print the confidence interval using the actual `confidenceLevel`
            print("{:.1f}% confidence interval for Bernoulli parameter p: [{:.3f}, {:.3f}]".format(
                confidence_level, interval[0], interval[1]
            ))
        except ValueError as e:
            print("Error:", e)

        print("\n-----------------Descriptive Statistics (Estimate Sigma)-----------------")
        confidence_level = 98  # e.g., 95 for 95% confidence level
        data2 = [113, 106, 102, 104, 112, 115, 103, 109]
        descriptive_stats2 = DesData(data2)
        try:
            ci = descriptive_stats2.var_ci(confidence_level)
            print("98% Confidence Interval for Variance: [{}, {}]".format(ci[0], ci[1]))
        except ValueError as e:
            print(e)

        print("\n-----------------InferentialStatistics-----------------")
        # Create an instance of InferentialStatistics with the data
        # inferential_stats = InferData(data)  # Uncomment if InferData is implemented

if __name__ == "__main__":
    StatisticsDemo.main()

