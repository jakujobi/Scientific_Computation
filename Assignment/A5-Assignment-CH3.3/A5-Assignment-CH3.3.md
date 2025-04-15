# John Akujobi - Math 374


---
## 2. If we use the secant method on $f(x) = x^3 - 2x + 2$   starting with $x_0 = 0$ and $x_1 = 1$, what is $x_2$?
1. First, we'll calculate $f (x_0)$ and $f (x_1)$:
   - $f (0) \quad = 0^3 - 2 (0) + 2  \quad  =0-0+2 \quad= 2$
   - $f (1) = 1^3 - 2 (1) + 2 = 1$
2. And i'll use the secant formula:
   $X_2 = x_1 - f (x_1) \cdot \frac{x_1 - x_0}{f (x_1) - f (x_0)} = 1 - 1 \cdot \frac{1 - 0}{1 - 2} = 1 + 1 = 2$

> [!success]
> $x_2 = {2}$

---
## 11. Show that if the iterates in Newton’s method converge to a point $r$ for which $f'(r) \neq 0$, then $f(r) = 0$.  Establish the same assertion for the secant method.  

*Hint:* In the latter, the Mean-Value Theorem of Differential Calculus is useful.  
This is the case $n = 0$ in Taylor’s Theorem.

**Newton’s Method**:
- Assume $x_n \to r$. The iteration is:
  $X_{n+1} = x_n - \frac{f (x_n)}{f' (x_n)}$
- Taking the limit $n \to \infty$:
  $R = r - \frac{f (r)}{f' (r)} \implies 0 = -\frac{f (r)}{f' (r)} \implies f (r) = 0$

**Secant Method**:
- Assume $x_n \to r$. The iteration is:
  $X_{n+1} = x_n - f (x_n) \cdot \frac{x_n - x_{n-1}}{f (x_n) - f (x_{n-1})}$
- By the Mean Value Theorem, $f (x_n) - f (x_{n-1}) = f' (c)(x_n - x_{n-1})$ for some $c$.
- As $n \to \infty$, $c \to r$, so:
  $X_{n+1} = x_n - \frac{f (x_n)}{f' (r)}$
- Taking the limit $n \to \infty$:
  $R = r - \frac{f (r)}{f' (r)} \implies f (r) = 0$

> [!success]
> For both methods, if $x_n \to r$ and $f' (r) \neq 0$, then $f (r) = 0$.

---
## 13 b. Test the sequence  $x_n = 2^{-n}$ for different types of convergence (i.e., linear, super linear, or quadratic), where $n = 1, 2, 3, \dots$.

**Linear Convergence**:
- Lemme check if $|x_{n+1}| \leq C |x_n|$ for $0 < C < 1$:
- $|x_{n+1}| = 2^{-(n+1)}$
- $= \frac{1}{2} \cdot 2^{-n}$
- $= \frac{1}{2} |x_n|$
- Well, $C = \frac{1}{2}$, so convergence is **linear**.
**Super linear**
- We need $\frac{|x_{n+1}|}{|x_n|} \to 0$.
- But $\frac{|x_{n+1}|}{|x_n|} = \frac{1}{2}$ (constant)
- So, not superlinear

**Quadratic**
 $|x_{n+1}| \leq C |x_n|^2$
 - $\frac{|x_{n+1}|}{|x_n|^2}$
 - $= \frac{2^{-(n+1)}}{(2^{-n})^2}$
 - $= 2^{n-1} \to \infty \quad$
 - It is not bounded, so it is not super linear

> [!success]
> The sequence $x_n = 2^{-n}$ converges **linearly** to 0.
> But it isn't super linear or quadratic


