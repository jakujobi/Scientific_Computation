import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Set page config first
st.set_page_config(page_title="Numerical Differentiation Analysis", layout="wide")

# Add CSS for better styling
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6;
    }
    .main .block-container {
        padding: 2rem;
    }
    h1 {
        color: #2a4a7d;
    }
    .st-expander {
        background: white;
        border: 1px solid #d6d6d6;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Title and introduction
st.title("Numerical Differentiation Error Analysis")
st.markdown("""
**Analyzing Forward and Central Difference Formulas for f(x) = sin(x) at x = 1**
""")

# Theory section in expanders
with st.expander("📚 Theoretical Background", expanded=True):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Forward Difference (Formula 1):**
        \[
        f'(x) \approx \frac{f(x+h) - f(x)}{h}
        \]
        - Truncation error: \( O(h) \)
        - Rounding error: \( O(\epsilon/h) \)
        """)
        
    with col2:
        st.markdown("""
        **Central Difference (Formula 2):**
        \[
        f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}
        \]
        - Truncation error: \( O(h^2) \)
        - Rounding error: \( O(\epsilon/h) \)
        """)

# Sidebar controls
with st.sidebar:
    st.header("Controls")
    h_min = st.slider("Minimum h (10^-k)", 1, 16, 1)
    h_max = st.slider("Maximum h (10^-k)", 1, 16, 16)
    num_points = st.slider("Number of points", 10, 100, 50)
    eps = st.number_input("Machine epsilon (ε)", 1e-16, 1e-10, 2.22e-16, format="%e")

# Calculation functions
def calculate_errors(h_values, eps):
    exact = np.cos(1.0)
    results = {'h': [], 'err1': [], 'err2': [], 
               'trunc1': [], 'trunc2': [], 
               'round1': [], 'round2': []}
    
    for h in h_values:
        # Forward difference
        f_plus = np.sin(1 + h)
        approx1 = (f_plus - np.sin(1)) / h
        err1 = abs(approx1 - exact)
        
        # Central difference
        f_minus = np.sin(1 - h)
        approx2 = (f_plus - f_minus) / (2 * h)
        err2 = abs(approx2 - exact)
        
        # Error bounds
        trunc1 = h/2
        trunc2 = h**2/6
        round1 = 2*eps/h
        round2 = eps/h
        
        results['h'].append(h)
        results['err1'].append(err1)
        results['err2'].append(err2)
        results['trunc1'].append(trunc1)
        results['trunc2'].append(trunc2)
        results['round1'].append(round1)
        results['round2'].append(round2)
        
    return results

# Generate h values
h_values = np.logspace(-h_max, -h_min, num_points)
results = calculate_errors(h_values, eps)

# Main visualization
st.header("Error Analysis Visualization")

col1, col2 = st.columns(2)

with col1:
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    ax1.loglog(results['h'], results['err1'], 'b-', label='Actual Error')
    ax1.loglog(results['h'], results['trunc1'], 'r--', label='Truncation Bound')
    ax1.loglog(results['h'], results['round1'], 'g--', label='Rounding Bound')
    ax1.set_title("Forward Difference Formula (1)")
    ax1.set_xlabel("h (log scale)")
    ax1.set_ylabel("Error (log scale)")
    ax1.grid(True, which='both')
    ax1.legend()
    st.pyplot(fig1)

with col2:
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    ax2.loglog(results['h'], results['err2'], 'b-', label='Actual Error')
    ax2.loglog(results['h'], results['trunc2'], 'r--', label='Truncation Bound')
    ax2.loglog(results['h'], results['round2'], 'g--', label='Rounding Bound')
    ax2.set_title("Central Difference Formula (2)")
    ax2.set_xlabel("h (log scale)")
    ax2.set_ylabel("Error (log scale)")
    ax2.grid(True, which='both')
    ax2.legend()
    st.pyplot(fig2)

# Error analysis section
st.header("Detailed Error Analysis")

# Optimal h calculations
opt_h1 = (2*eps)**0.5
opt_h2 = (3*eps)**(1/3)

col1, col2 = st.columns(2)
with col1:
    st.markdown(f"""
    **Forward Difference Optimal h:**
    \[
    h_{{opt}} = \sqrt{{2\epsilon}} \approx {opt_h1:.2e}
    \]
    - Minimum achievable error: {np.sqrt(2*eps)/2:.2e}
    """)

with col2:
    st.markdown(f"""
    **Central Difference Optimal h:**
    \[
    h_{{opt}} = \sqrt[3]{{3\epsilon}} \approx {opt_h2:.2e}
    \]
    - Minimum achievable error: {(3*eps)**(2/3)/6:.2e}
    """)

# Comparison section
st.header("Comparison of Methods")
st.markdown("""
| Aspect                | Forward Difference | Central Difference |
|-----------------------|--------------------|--------------------|
| Truncation Error Order | O(h)               | O(h²)              |
| Rounding Error Order   | O(ε/h)             | O(ε/h)             |
| Optimal h             | ~√ε                | ~∛ε                |
| Best Accuracy         | ~√ε                | ~ε^{2/3}           |
| Stability             | Moderate           | Better             |

**Key Observations:**
1. Central difference provides better accuracy for same h
2. Central difference maintains stability for larger h values
3. Forward difference deteriorates faster for small h
""")

# Run with: streamlit run app.py