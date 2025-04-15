### **1. Understanding Numerical Differentiation**

#### **What is a derivative?**

The derivative measures how a function changes as its input changes:
$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$
In practice, we can't use \( h = 0 \), so we approximate it with small \( h \).

---

### **2. The Two Formulas**

#### **Formula 1: Forward Difference**

$f'(x) \approx \frac{f(x+h) - f(x)}{h}
$

- Uses 1 point ahead of \( x \)
- Simple but less accurate

#### **Formula 2: Central Difference**

$f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}
$

- Uses points on both sides of \( x \)
- More accurate but requires more computation

---

### **Key Concepts You Need**

#### **a. Taylor Series Expansion** (Core Tool)

Expresses functions as infinite sums:
$f(x+h) = f(x) + hf'(x) + \frac{h^2}{2}f''(x) + \cdots$
This helps analyze approximation errors.

#### **b. Truncation Error**

Error from cutting off infinite series in approximations.

- For Formula 1: Truncation error \(\propto h\) (linear)
- For Formula 2: Truncation error \(\propto h^2\) (quadratic)

#### **c. Rounding Error**

Computers have finite precision (machine epsilon $\epsilon \approx 2.22 \times 10^{-16}$).
When \( h \) is very small:
$\text{Rounding error} \propto \frac{\epsilon}{h}
$

---

### **Step-by-Step Analysis**

#### **Task 1: Truncation Error Bounds**

**Formula 1:**

1. Taylor expand \( f(x+h) \):
   
   f(x+h) = f(x) + hf'(x) + \frac{h^2}{2}f''(\xi)$

2. Rearrange for \( f'(x) \):
   $f'(x) = \frac{f(x+h)-f(x)}{h} - \frac{h}{2}f''(\xi)$

3. Truncation error bound:
   $|E_{\text{trunc}}| \leq \frac{h}{2} |f''(\xi)| \leq \frac{h}{2} \quad (\text{since } |\sin''(x)| \leq 1)$

**Formula 2:**

1. Expand both \( f(x+h) \) and \( f(x-h) \):
   $f(x+h) - f(x-h) = 2hf'(x) + \frac{h^3}{3}f'''(\xi)$
2. Truncation error bound:
   $|E_{\text{trunc}}| \leq \frac{h^2}{6} |f'''(\xi)| \leq \frac{h^2}{6}$

---

#### **Task 2: Rounding Error Bounds**

Assume $\tilde{f}(x) = f(x)(1 + \delta)$ where $|\delta| \leq \epsilon$.

**Formula 1:**
$\text{Rounding error} \leq \frac{2\epsilon |f(x)|}{h} \approx \frac{2\epsilon}{h}$

**Formula 2:**
$\text{Rounding error} \leq \frac{\epsilon}{h}$

---

#### **Task 3: Total Error & Visualization**

Total error = Truncation error + Rounding error

**For Formula 1:**
$\text{Total Error} \approx \frac{h}{2} + \frac{2\epsilon}{h}$

**For Formula 2:**
$\text{Total Error} \approx \frac{h^2}{6} + \frac{\epsilon}{h}$

**Why log-log plots?**

- \( h \) varies over many orders of magnitude (10^{-1}$ to 10^{-16}$)
- Errors also span many orders
- Logarithmic scales compress wide ranges into manageable plots.

---

### **5. Optimal \( h \)**

Find \( h \) that minimizes total error.

**Formula 1:**
Set derivatives equal:
$\frac{d}{dh}\left(\frac{h}{2} + \frac{2\epsilon}{h}\right) = 0 \Rightarrow h_{\text{opt}} = 2\sqrt{\epsilon}$

**Formula 2:**
$\frac{d}{dh}\left(\frac{h^2}{6} + \frac{\epsilon}{h}\right) = 0 \Rightarrow h_{\text{opt}} = \sqrt[3]{3\epsilon}$

---

### **6. Python Implementation Walkthrough**

#### **Key Libraries:**

- `numpy`: Numerical calculations
- `matplotlib`: Plotting
- `streamlit`: Interactive web app

#### **Code Structure:**

1. **Compute Exact Derivative:**
   
   ```python
   exact_deriv = np.cos(1.0)  # Since d/dx(sin(x)) = cos(x)
   ```

2. **Error Calculations:**
   
   ```python
   # Forward difference
   approx1 = (np.sin(1 + h) - np.sin(1)) / h
   error1 = abs(approx1 - exact_deriv)
   ```

3. **Plotting:**
   
   ```python
   plt.loglog(h_values, error1, label='Actual Error')
   ```

---

### **7. Why Streamlit?**

- Creates interactive web apps directly from Python
- Lets users adjust parameters (e.g., \( h \) range)
- Displays visualizations and theory side-by-side

---

### **8. Common Pitfalls & Solutions**

#### **Problem 1: Underflow/Overflow**

- **Solution:** Use log scales and avoid \( h = 0 \)

#### **Problem 2: Choosing \( h \)**

- **Solution:** Follow optimal \( h \) formulas

#### **Problem 3: Finite Precision**

- **Solution:** Understand that smaller \( h \) ≠ better accuracy due to rounding errors

---

### **9. Final Comparison Table**

| Aspect                 | Forward Difference | Central Difference |
| ---------------------- | ------------------ | ------------------ |
| Truncation Error       | $O(h)$             | $O(h^2)$           |
| Rounding Error         | $O(\epsilon/h)$    | $O(\epsilon/h)$    |
| Optimal\( h \)         | $10^{-8}$          | $10^{-5}$          |
| Best Accuracy Achieved | $10^{-8}$          | $10^{-11}$         |

---

### **What I did**

1. **Implement the Code:**
   
   - Use the provided Streamlit template
   - Verify calculations match theoretical bounds

2. **Experiment:**
   
   - Try different functions (e.g., $f(x) = e^x$)
   - Compare with other differentiation formulas

3. **Deepen Understanding:**
   
   - Read about Richardson Extrapolation
   - Explore automatic differentiation
