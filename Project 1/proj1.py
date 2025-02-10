import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Numerical Differentiation Error Analysis")
st.markdown("""
This interactive app compares two numerical differentiation formulas for approximating the derivative of \( \sin(x) \) at \( x=1 \):

1. **Forward Difference:** \( f'(x) \approx \frac{f(x+h)-f(x)}{h} \)
2. **Central Difference:** \( f'(x) \approx \frac{f(x+h)-f(x-h)}{2h} \)

The app calculates the actual error, truncation error, rounding error, and their sum (total error) as \( h \) varies from \( 10^{-1} \) to \( 10^{-16} \).
""")

# Define the function and its true derivative
def f(x):
    return np.sin(x)

def true_derivative(x):
    return np.cos(x)

# Set the point of interest
x = 1.0
true_val = true_derivative(x)

# Machine epsilon for double precision
u = np.finfo(float).eps

# Create h values: h = 10^{-k} for k = 1, ..., 16
k_values = np.arange(1, 17)
h_values = 10.0 ** (-k_values)

# Initialize arrays to store errors for forward and central differences
errors_forward = np.zeros_like(h_values)
errors_central = np.zeros_like(h_values)

# Arrays for truncation and rounding error estimates
trunc_forward = np.zeros_like(h_values)
round_forward = np.zeros_like(h_values)
total_forward = np.zeros_like(h_values)

trunc_central = np.zeros_like(h_values)
round_central = np.zeros_like(h_values)
total_central = np.zeros_like(h_values)

# Theoretical constants based on Taylor series expansion at x=1
const_forward = 0.5 * abs(np.sin(x))       # For forward difference: truncation error ~ (h/2)|sin(1)|
const_central = abs(np.cos(x)) / 6.0         # For central difference: truncation error ~ (h^2/6)|cos(1)|

# Loop over h values and compute errors
for i, h in enumerate(h_values):
    # Forward difference approximation
    derivative_forward = (f(x + h) - f(x)) / h
    errors_forward[i] = abs(derivative_forward - true_val)
    
    # Central difference approximation
    derivative_central = (f(x + h) - f(x - h)) / (2 * h)
    errors_central[i] = abs(derivative_central - true_val)
    
    # Truncation error estimates
    trunc_forward[i] = const_forward * h
    trunc_central[i] = const_central * h**2
    
    # Rounding error estimates: error ~ (sum of function values)*u/h (with appropriate factors)
    round_forward[i] = (abs(f(x + h)) + abs(f(x))) * u / h
    round_central[i] = (abs(f(x + h)) + abs(f(x - h))) * u / (2 * h)
    
    # Total error as the sum of truncation and rounding errors
    total_forward[i] = trunc_forward[i] + round_forward[i]
    total_central[i] = trunc_central[i] + round_central[i]

# Let the user choose which method to view
method = st.selectbox("Select the Differentiation Method", ("Forward Difference", "Central Difference"))

if method == "Forward Difference":
    errors = errors_forward
    trunc = trunc_forward
    rounding = round_forward
    total = total_forward
    title = "Forward Difference: \\(\\frac{f(x+h)-f(x)}{h}\\)"
else:
    errors = errors_central
    trunc = trunc_central
    rounding = round_central
    total = total_central
    title = "Central Difference: \\(\\frac{f(x+h)-f(x-h)}{2h}\\)"

# Plotting the results using a log-log scale
fig, ax = plt.subplots(figsize=(8, 6))
ax.loglog(h_values, errors, 'ko-', label='Actual Error')
ax.loglog(h_values, trunc, 'r--', label='Truncation Error Bound')
ax.loglog(h_values, rounding, 'b--', label='Rounding Error Bound')
ax.loglog(h_values, total, 'g--', label='Total Error Estimate')
ax.set_xlabel(r'$h$')
ax.set_ylabel(r'$|\text{error}|$')
ax.set_title(title)
ax.legend()
ax.grid(True, which="both", ls=":")

st.pyplot(fig)

st.markdown("""
### Discussion:
- **Truncation Error:**  
  For the forward difference, it is \( O(h) \) (proportional to \( h \)), and for the central difference, it is \( O(h^2) \) (proportional to \( h^2 \)).
- **Rounding Error:**  
  Due to finite precision (machine epsilon \( u \)), the subtraction in the difference formulas introduces rounding errors that behave roughly as \( O(1/h) \).
- **Total Error:**  
  The sum of the truncation and rounding errors shows a minimum at an optimal \( h \). This optimal point represents a balance between decreasing truncation error and increasing rounding error as \( h \) decreases.
""")
