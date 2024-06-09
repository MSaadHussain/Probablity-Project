import numpy as np
import scipy.stats as stats

def binomial_distribution(n, p, k):
    probability = stats.binom.pmf(k, n, p)
    return probability

def poisson_distribution(mu, k):
    probability = stats.poisson.pmf(k, mu)
    return probability

def normal_distribution(mean, std_dev, x):
    probability = stats.norm.pdf(x, mean, std_dev)
    return probability

def main():
    print("Choose a distribution:")
    print("1. Binomial Distribution")
    print("2. Poisson Distribution")
    print("3. Normal Distribution")
    
    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        n = int(input("Enter the number of trials (n): "))
        p = float(input("Enter the probability of success (p): "))
        k = int(input("Enter the number of successes (k): "))
        probability = binomial_distribution(n, p, k)
        print(f"Probability of getting {k} successes in {n} trials: {probability:.6f}")

    elif choice == 2:
        mu = float(input("Enter the average rate (mu): "))
        k = int(input("Enter the number of occurrences (k): "))
        probability = poisson_distribution(mu, k)
        print(f"Probability of {k} occurrences with average rate {mu}: {probability:.6f}")

    elif choice == 3:
        mean = float(input("Enter the mean: "))
        std_dev = float(input("Enter the standard deviation: "))
        x = float(input("Enter the value (x): "))
        probability = normal_distribution(mean, std_dev, x)
        print(f"Probability density function at {x} with mean {mean} and standard deviation {std_dev}: {probability:.6f}")

    else:
        print("Invalid choice. Please choose a number between 1 and 3.")

if __name__ == "__main__":
    main()
