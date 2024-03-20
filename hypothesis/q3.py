from scipy.stats import ttest_1samp
import numpy as np

# Given data
sample_mean = 7  # sample mean
population_mean = 8  # hypothesized population mean
sample_std = 2  # sample standard deviation
sample_size = 30  # sample size
significance_level = 0.05

# Create a synthetic dataset based on the provided mean, std, and size
np.random.seed(42)  # Setting seed for reproducibility
data = np.random.normal(loc=sample_mean, scale=sample_std, size=sample_size)


# Calculate the t-score
t_score = (sample_mean - population_mean) / (sample_std / np.sqrt(sample_size))

# Perform one-tailed t-test
t_statistic, p_value = ttest_1samp(data, population_mean)

# Determine if there is evidence to suggest that the average recovery time is significantly less than 8 days
if p_value < significance_level / 2:  # one-tailed test
    print("Reject the null hypothesis. There is evidence to suggest that the average recovery time is significantly less than 8 days.")
else:
    print("Fail to reject the null hypothesis. There is no evidence to suggest that the average recovery time is significantly less than 8 days.")
