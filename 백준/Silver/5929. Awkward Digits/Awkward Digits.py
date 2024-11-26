def generate_candidates(base_string, base):
    """
    Generate all possible numbers by flipping one digit of a given base representation.
    """
    candidates = set()
    for i, char in enumerate(base_string):
        original_digit = int(char)
        for replacement in range(base):
            if replacement != original_digit:
                # Replace the digit at position i
                new_representation = (
                    base_string[:i] + str(replacement) + base_string[i + 1:]
                )
                # Convert to decimal and store
                candidates.add(int(new_representation, base))
    return candidates


def find_correct_number(base2_str, base3_str):
    """
    Determine the correct decimal number based on the wrong base-2 and base-3 strings.
    """
    # Generate possible values for base-2 and base-3
    base2_candidates = generate_candidates(base2_str, 2)
    base3_candidates = generate_candidates(base3_str, 3)

    # Find intersection
    correct_number = base2_candidates.intersection(base3_candidates)
    
    # There should be exactly one correct number
    assert len(correct_number) == 1, "There must be a unique solution."
    return correct_number.pop()


# Input and Output
if __name__ == "__main__":
    # Read input
    base2_str = input().strip()
    base3_str = input().strip()

    # Solve the problem
    result = find_correct_number(base2_str, base3_str)
    print(result)