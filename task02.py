import sys
import random

def main(num_simulations):
    # Number of successful simulations (where all children are girls)
    num_successes = 0

    for i in range(num_simulations):
        # Generate the genders of the children
        children = [random.choice(["girl", "boy"]) for _ in range(3)]

        # Check if at least one child is a girl and all children are girls
        if "girl" in children and all(child == "girl" for child in children):
            num_successes += 1

    # Calculate and print the probability
    probability = num_successes / num_simulations
    print(f"Probability: {probability:.2f}")

if __name__ == "__main__":
    # Get the number of simulations from the command line argument
    num_simulations = int(sys.argv[1])

    main(num_simulations)
