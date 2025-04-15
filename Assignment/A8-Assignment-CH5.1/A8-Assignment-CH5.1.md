
# **Problem 11** - Obtain an upper bound on the absolute error when we compute $\int_0^6 \sin(x^2) , dx$ by means of the composite trapezoid rule using 101 equally spaced points.

1. **Number of subintervals and step size:**
   - $101$ points 
   - Gives us 100 subintervals ($n = 100$).
   - So, our step size will be
      - Step size $h = \frac{6 - 0}{100}$
      - $= 0.06$.

2. **Error formula for composite trapezoid rule:**
   - Absolute error bound: $\left| E \right| \leq \frac{1}{12}(b - a) h^2 \max_{\xi \in [a, b]} |f''(\xi)|$.

1. **Second derivative of $f(x) = \sin(x^2)$:**
	- $f''(x) = 2\cos(x^2) - 4x^2 \sin(x^2)$.
	- Max of $|f''(x)|$ on $[0, 6]$:
		- Approximate $\max |f''(x)| \leq 2 + 4(6)^2 = 146$.

2. **Compute the error bound:**
   - $\left| E \right| \leq \frac{1}{12} \times 6 \times (0.06)^2 \times 146 = 0.2628$.

Aaand the answer is 0.2628

---
# **Problem 17** - Compute two approximate values for $\int_1^2 \frac{dx}{x^2}$ using $h = \frac{1}{2}$ with the composite trapezoid rule.

1. **First, lets get the step size and subintervals:**
   - $h = \frac{1}{2}$
   - partition points will be: $1$, $1.5$, $2$.

2. **Composite trapezoid rule formula:**
   - $T = \frac{h}{2} \left[ f(1) + 2f(1.5) + f(2) \right]$.

- **Lets evaluate $f(x) = \frac{1}{x^2}$ at partition points (using scientific calculator):**
	- $f(1) = 1$
	- $f(1.5) = \frac{4}{9}$
	- $f(2) = \frac{1}{4}$

- **Compute the approximation:**
	- $T = \frac{1/2}{2} \left[ 1 + 2 \left( \frac{4}{9} \right) + \frac{1}{4} \right]$
	- $= \frac{77}{144} \approx 0.5347$.

---
# **Problem 18** - Consider $\int_1^2 \frac{dx}{x^3}$. What is the result of using the composite trapezoid rule with the partition points - $1$, $\frac{3}{2}$, and $2$?

1. **Partition points:**
   - Subintervals: $[1, \frac{3}{2}]$ and $[\frac{3}{2}, 2]$.

2. **Composite trapezoid rule formula:**
   - $T = \frac{h}{2} \left[ f(1) + 2f\left(\frac{3}{2}\right) + f(2) \right]$, where $h = \frac{1}{2}$.

1. **Evaluate $f(x) = \frac{1}{x^3}$ at partition points:
2. Still using the scientific calculator since it makes it faster**
   - $f(1) = 1$
   - $f\left(\frac{3}{2}\right) = \frac{8}{27}$
   -  $f(2) = \frac{1}{8}$

1. **Compute the approximation:**
   - $T = \frac{1/2}{2} \left[ 1 + 2 \left( \frac{8}{27} \right) + \frac{1}{8} \right]$
   - $= \frac{371}{864} \approx 0.4294$.

---