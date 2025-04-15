
---
# MATH 373 Project 2 (150 points)
**Due on 10:50 AM of March 21st, 2025**  
**Please submit your report, source codes, and environment which TA can run your codes**

---
## Problem Description
Implement the **bisection**, **Newton**, and **secant** methods for solving nonlinear equations in one dimension, and test your implementations by finding at least one root for each of the following equations:
- $f_1(x) = x^2 - 4\sin(x)$             (1)
- $f_2(x) = x^2 - 1$                       (2)
- $f_3(x) = x^3 - 3x^2 + 3x - 1$     (3)

---
## Questions to Address
1. **What termination criterion should you use?**
2. **What convergence rate is achieved in each case?**
3. **Compare your results (solutions and convergence rates).**

---
## Considerations
- We are implementing it using python and streamlit and hosted on streamlit
- Developing on the vscode ide on a windows 11 machine and using github as a version control system
- We will need to make the project report as detailed as possible and write a kind of paper on it.
- The report will be integrated into the webapp
- We must have a lot of visualizations
- The entire thing must be well explained
- You can make it interactive where needed
---
# Pseudocodes
## SECANT METHOD
Algorithm 1: A Pseudocode for Secant Method
#### INPUT
- Function: $f$
- Initial values: $a$, $b$
- Maximum iterations: $nmax$
- Convergence tolerances: $\delta_1$, $\delta_2$
- Variables: $n$, $fa$, $fb$, $\delta_1$, $\delta_2$, $d$
### Algorithm Steps
```plaintext
1. Initialize:
   fa ← f(a)
   fb ← f(b)

2. If |fb| < |fa|, then:
      Swap a and b
      Swap fa and fb

3. OUTPUT 0, a, fa
4. OUTPUT 1, b, fb

5. For k = 2 to nmax do:
   a. If |fb| < |fa|, then:
         Swap a and b
         Swap fa and fb

   b. Compute:
         d ← (b - a) / (fb - fa)
         b ← a
         fb ← fa
         d ← d * fa
         a ← a - d
         fa ← f(a)

   c. OUTPUT n, a, fa

   d. Check convergence:
         If |d| < δ₁ or |fa| < δ₂ then:
            OUTPUT "converge"
            RETURN
```

### Explanation
- This algorithm iteratively approximates the root of $f(x)$ using the secant method.
- It ensures **numerical stability** by always choosing the value with a smaller function magnitude.
- The stopping criterion is checked based on **tolerance limits** $\delta_1$ and $\delta_2$.
---
## BISECTION ALGORITHM
Algorithm 1: A Pseudocode for the Bisection Method
### INPUT
- Interval endpoints: $a, b$
- Maximum iterations: $M$
- Error tolerances: $\delta, \epsilon$
- Variables: $u, v, w, e, c$

### Algorithm Steps
```plaintext
1. Compute:
   u ← f(a)
   v ← f(b)
   e ← b - a

2. OUTPUT: a, b, u, v

3. If sign(u) = sign(v), then:
      Stop

4. For k = 1 to M do:
   a. Update error:
         e ← e / 2
         c ← a + e
         w ← f(c)

   b. OUTPUT: k, c, w, e

   c. Check convergence:
         If |e| < δ or |w| < ε then:
            Stop

   d. Check sign change:
         If sign(w) ≠ sign(u), then:
            b ← c
            v ← w
         Else:
            a ← c
            u ← w
```

### Explanation
- This algorithm **iteratively reduces the interval size** where the function changes sign.
- It **halts** when the error bound is **less than the defined tolerance** $\delta$ or function value magnitude is **less than** $\epsilon$.
- The midpoint **$c$** is used to **refine the interval** at each step.
- The function values are tracked to determine the **new interval** for the next iteration.

---
## NEWTON’S METHOD
Algorithm 1: A Pseudocode for Newton’s Method
### INPUT
- Function and its derivative: $f, f'$
- Initial guess: $x$
- Maximum iterations: $nmax$
- Error tolerances: $\delta_1, \delta_2, \epsilon$
- Variables: $fx, fp, d$

### Algorithm Steps
```plaintext
1. Compute:
   fx ← f(x)

2. OUTPUT: 0, x, fx

3. For k = 1 to nmax do:
   a. Compute derivative:
         fp ← f'(x)

   b. Check if derivative is too small:
         If |fp| < ε then:
            OUTPUT "small derivative"
            RETURN

   c. Compute update step:
         d ← fx / fp
         x ← x - d
         fx ← f(x)

   d. OUTPUT: n, x, fx

   e. Check convergence:
         If |d| < δ1 or |fx| < δ2 then:
            OUTPUT "converge"
            RETURN
```

---
### Explanation
- Newton's method iteratively **updates the estimate** for the root.
- The stopping criteria ensure that:
    - The update step $d$ is **small enough** ($|d| < \delta_1$).
    - The function value **approaches zero** ($|fx| < \delta_2$).
- If the derivative is **too small** ($|f'(x)| < \epsilon$), the method stops early to **avoid division by zero**.
- The algorithm **refines the estimate** $x$ using the Newton-Raphson formula.

---
