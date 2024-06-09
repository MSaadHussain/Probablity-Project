def bayes_theorem(prior_A, likelihood_B_given_A, prior_not_A, likelihood_B_given_not_A):
    numerator = likelihood_B_given_A * prior_A
    denominator = (likelihood_B_given_A * prior_A) + (likelihood_B_given_not_A * prior_not_A)
    return numerator / denominator

def main():
    print("Bayes' Theorem Calculator")
    print("P(A|B) = [P(B|A) * P(A)] / [P(B|A) * P(A) + P(B|¬A) * P(¬A)]")
    
    prior_A = float(input("Enter the prior probability of A (P(A)): "))
    likelihood_B_given_A = float(input("Enter the likelihood of B given A (P(B|A)): "))
    prior_not_A = float(input("Enter the prior probability of not A (P(¬A)): "))
    likelihood_B_given_not_A = float(input("Enter the likelihood of B given not A (P(B|¬A)): "))
    
    posterior = bayes_theorem(prior_A, likelihood_B_given_A, prior_not_A, likelihood_B_given_not_A)
    
    print(f"\nPosterior probability (P(A|B)): {posterior:.4f}")

if __name__ == "__main__":
    main()
