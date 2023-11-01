# The truth table for XNOR gate
import itertools

# Header for the truth table
print("The truth table for XNOR gate is:")
print("A\tB\tResult")

# Generate all possible input combinations (True and False)
input_comb = list(itertools.product([True, False], repeat=2))

# Evaluate and print the truth table for the XNOR gate
for combination in input_comb:
    A, B = combination
    result = not (A ^ B) # XNOR operation
    print(f"{int(A)}\t{int(B)}\t{int(result)}")
