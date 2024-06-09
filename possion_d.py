class DiscreteDistribution:
    def __init__(self, distribution):
        self.distribution = distribution

    def probability(self, outcome):
        return self.distribution.get(outcome, 0)

    def expected_value(self):
        return sum(outcome * probability for outcome, probability in self.distribution.items())

def main():
    print("Enter your discrete probability distribution.")
    print("Format: outcome1:probability1,outcome2:probability2,...")
    
    distribution_input = input("Enter your distribution: ")
    distribution = dict(item.split(":") for item in distribution_input.split(","))
    distribution = {int(k): float(v) for k, v in distribution.items()}
    
    dist = DiscreteDistribution(distribution)

    while True:
        print("\nChoose an option:")
        print("1. Calculate expected value")
        print("2. Exit")

        choice = int(input("Enter your choice (1-2): "))

        if choice == 1:
                        print(f"Expected value: {dist.expected_value()}")
        elif choice == 2:
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
