import math

def BE1(A):
    return 0.06446 * A**(2/3)

def BE2(A):
    return 0.05940 * A**(4/3)

def BE3(A):
    return 0.05940 * A**(2)

def BE4(A):
    return 0.0628 * A**(8/3)

def BE5(A):
    return 0.0693 * A**(10/3)

def BM1(A):
    return 1.790

def BM2(A):
    return 1.650 * A**(2/3)

def BM3(A):
    return 1.650 * A**(4/3)

def BM4(A):
    return 1.746 * A**(2)

def BM5(A):
    return 1.926 * A**(8/3)

def TE1(A):
    return 1.023 * 10 ** 14 * A**(2/3)

def TE2(A):
    return 7.265 * 10** 7 * A**(4/3)

def TE3(A):
    return 3.385 * 10** 1 * A**(2)

def TE4(A):
    return 1.0649 * 10** (-5) * A**(8/3)

def TE5(A):
    return 2.395 * 10** (-12) * A**(10/3)

def TM1(A):
    return 3.184 * 10** 13

def TM2(A):
    return 2.262 * 10 ** 7 * A**(2/3)

def TM3(A):
    return 1.054 * 10** 1 * A**(4/3)

def TM4(A):
    return 3.276 * 10** (-6) * A**(2)

def TM5(A):
    return 7.367 * 10** (-13) * A**(8/3)

# Taking input from the user
mu_pol = input("Enter the type of transition: ")

# Assuming half_life is a numeric input, you can modify this part based on your actual input requirement
try:
    half_life = float(input("Enter the half-life: "))
except ValueError:
    print("Invalid input. Please enter a valid numerical value for half-life.")
    exit()
A = int(input("Enter the value of A: "))

# Create a dictionary to map the user input to the corresponding functions
transition_functions = {
    'E1': BE1,
    'E2': BE2,
    'E3': BE3,
    'E4': BE4,
    'E5': BE5,
    'M1': BM1,
    'M2': BM2,
    'M3': BM3,
    'M4': BM4,
    'M5': BM5,
}

# Check if the user input is valid
if mu_pol in transition_functions:
    total_transition_prob = 0.693 / half_life
    reduced_transition_prob = transition_functions[mu_pol](A)

    print("Total Transition Probability:", total_transition_prob)
    print(f"Reduced Transition probability for {mu_pol}:", reduced_transition_prob)
else:
    print("Invalid transition type. Please enter a valid value.")
