# Study-of-isomeric-state

This Python program calculates the total transition probability and reduced transition probability for the nuclear structure based on the user input. This program uses different equations depending on the type of transition. 

The program provides the following five different types of Electric and Magnetic transitions with respective formulas : 

* **Electric Transitions**:

  * `E1`: $0.06446 \times A^{2/3}$
  * `E2`: $0.05940 \times A^{4/3}$
  * `E3`: $0.05940 \times A^{2}$
  * `E4`: $0.0628 \times A^{8/3}$
  * `E5`: $0.0693 \times A^{10/3}$

* **Magnetic Transitions**:

  * `M1`: $1.790$
  * `M2`: $1.650 \times A^{2/3}$
  * `M3`: $1.650 \times A^{4/3}$
  * `M4`: $1.746 \times A^{2}$
  * `M5`: $1.926 \times A^{8/3}$


The program uses the half-life values to calculate the total transition probability and applies the relevant formula based on the transition type selected by the user.

## Input

The program requires the following user inputs:

1. **Type of Transition**: The user specifies the transition type, which can be one of the following:

   * `E1`, `E2`, `E3`, `E4`, `E5` (Electric transitions)
   * `M1`, `M2`, `M3`, `M4`, `M5` (Magnetic transitions)

2. **Half-life**: A numeric input representing the half-life of the isotope. The program uses this to calculate the total transition probability.

3. **Value of A**: An integer value representing the atomic mass number.

