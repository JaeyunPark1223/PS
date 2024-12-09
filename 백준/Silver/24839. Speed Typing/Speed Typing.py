# Optimized Code
T = int(input())

for case_number in range(1, T + 1):
    a = input()
    b = input()
    A = len(a)
    B = len(b)

    # Check if all characters in 'a' are the same
    if all(char == a[0] for char in a):
        # Count occurrences of the same character in 'b'
        count_in_b = b.count(a[0])
        if count_in_b >= A:
            print(f"Case #{case_number}: {B - A}")
        else:
            print(f"Case #{case_number}: IMPOSSIBLE")
    else:
        # Two pointers technique to match 'a' with 'b'
        i = 0  # Pointer for 'a'
        j = 0  # Pointer for 'b'
        while i < A and j < B:
            if a[i] == b[j]:
                i += 1
            j += 1
        
        if i == A:  # All characters in 'a' were matched
            print(f"Case #{case_number}: {B - A}")
        else:
            print(f"Case #{case_number}: IMPOSSIBLE")
