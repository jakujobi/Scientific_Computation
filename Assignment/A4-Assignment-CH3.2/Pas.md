**Problem 1: Verify Newton’s method for \(\sqrt{R}\)**

Newton's method for solving \(x^2 = R\) starts with \(f (x) = x^2 - R\). The iteration formula is:
$X_{n+1} = x_n - \frac{f (x_n)}{f' (x_n)} = x_n - \frac{x_n^2 - R}{2 x_n} = \frac{1}{2} \left ( x_n + \frac{R}{x_n} \right)$
Verified.

---

**Problem 2: Show \(x_{n+1}^2 - R = \frac{x_n^2 - R}{2 x_n}\)**

Using the iteration formula:
$X_{n+1} = \frac{1}{2} \left ( x_n + \frac{R}{x_n} \right)$
Square both sides:
$X_{n+1}^2 = \frac{1}{4} \left ( x_n^2 + 2 R + \frac{R^2}{x_n^2} \right)$
Subtract \(R\):
$X_{n+1}^2 - R = \frac{1}{4} \left ( x_n^2 - 2 R + \frac{R^2}{x_n^2} \right) = \frac{(x_n^2 - R)^2}{4 x_n^2}$
The problem statement may have a typo; the correct relation is quadratic in the error.

---

**Problem 13 b: Newton’s method for \(b (x) = \frac{1}{x^3} - \frac{1}{R}\)**

The iteration formula is:
$X_{n+1} = x_n - \frac{b (x_n)}{b' (x_n)} = x_n \cdot \frac{4 R - x_n^3}{3 R}$
**Restrictions:** \(x_0 \neq 0\) and close to \(R^{1/3}\).

---

**Problem 13 d: Newton’s method for \(d (x) = x - \frac{R}{x^2}\)**

The iteration formula is:
$X_{n+1} = \frac{3 R x_n}{x_n^3 + 2 R}$
**Restrictions:** \(x_0 > 0\).

---

**Problem 14: Newton’s method for \(f (x) = x - e^{x/l}\)**

The iteration formula is:
$$X_{n+1} = \frac{e^{x_n/l} (l - x_n)}{l - e^{x_n/l}}$$
**Behavior:** For \(l > e\), two roots exist. Convergence depends on \(x_0\). For \(l \leq e\), iterates may diverge.

---

**Problem 18: Newton’s formula for \(\sqrt[3]{N/M}\)**

For \(R = N/M\), the iteration is:
$X_{n+1} = \frac{2 x_n + \frac{N}{M x_n^2}}{3}$

---

**Problem 25: Iterations for \(\sqrt{2}\)**

**Newton's Method:**
- $(x_0 = 1): (x_1 = 1.5)$
- $(x_1 = 1.5): (x_2 \approx 1.4167)$
- $(x_2 \approx 1.4167): (x_3 \approx 1.4142)$
- **Accuracy \(10^{-6}\):** 4 iterations needed.

**Bisection Method:**  
Interval \([1, 2]\), each iteration halves the error.
- **Iterations needed:**  $\log_2 (10^6) \approx 20$.

**Final Answer:** Newton's method requires **4 iterations**, bisection requires **20 iterations** for \(10^{-6}\) accuracy.