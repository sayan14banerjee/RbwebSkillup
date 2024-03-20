from scipy.stats import norm

# Significance level (alpha) for a one-tailed test
alpha = 0.05

# Find the Z-score for the lower tail
z_score = norm.ppf(alpha)

print("Z-score for lower tail (one-tailed test):", z_score)
