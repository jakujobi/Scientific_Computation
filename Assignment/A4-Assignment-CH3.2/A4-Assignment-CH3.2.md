
# John Akujobi - Math 374
# 1.  Verify that when Newton’s method is used to compute $\sqrt{R}$ (by solving the equation $x^2 = R$), the sequence of iterates is defined by $x_{n+1} = \frac{1}{2} \left(x_n + \frac{R}{x_n} \right)$
I want to solve $X^2 - R = 0$
- First, for Newton’s method we set
	- $f(x) = x^2 - R,\quad f' (x) = 2 x$
- Iterating the formula
	- $X_{n+1} = x_n - \frac{f (x_n)}{f' (x_n)}$
	- $= x_n - \frac{x_n^2-R}{2 x_n}$
	- $= \frac{2 x_n^2 - (x_n^2-R)}{2 x_n}$
	- $= \frac{x_n^2 + R}{2 x_n}$
	- $= \frac{1}{2}\left (x_n + \frac{R}{x_n}\right)$
> [!success]
> Our formula is gonna be
$${x_{n+1} = \frac{1}{2}\left (x_n + \frac{R}{x_n}\right)}$$

---
# 2. (Continuation) Show that if the sequence ${x_n}$ is defined as in the preceding exercise, then $x_{n+1}^2 - R = \frac{x_n^2 - R}{2x_n}$
- Using the iteration formula:
	- $X_{n+1} = \frac{1}{2} \left ( x_n + \frac{R}{x_n} \right)$
- Square both sides:-
	- $X_{n+1}^2 = \frac{1}{4} \left ( x_n^2 + 2 R + \frac{R^2}{x_n^2} \right)$
- Subtract \(R\) 
	- $X_{n+1}^2 - R = \frac{1}{4} \left ( x_n^2 - 2 R + \frac{R^2}{x_n^2} \right)$
	- $= \frac{(x_n^2 - R)^2}{4 x_n^2}$

---
# 13. Each of the following functions has $\sqrt[3]{R}$ as a zero for any positive real number $R$. Determine the formulas for Newton’s method for each and any necessary restrictions on the choice for $x_0$.
## b. $b(x) = 1/x^3 - 1/R$

- Find the derivative: 
	- $b' (x) = -\frac{3}{x^4}$
- Apply Newton’s method:
	- $x_{n+1} = x_n - \frac{b (x_n)}{b' (x_n)}$
	- $= x_n - \frac{\frac{1}{x_n^3}-\frac{1}{R}}{-\frac{3}{x_n^4}}$
	- $= x_n + \frac{x_n^4}{3}\left (\frac{1}{x_n^3}-\frac{1}{R}\right)$.
	- $= x_n + \frac{x_n}{3}\left (1-\frac{x_n^3}{R}\right)$.
	- $= x_n + \frac{x_n}{3} - \frac{x_n^4}{3R})$.
- Simplified to
	- $= x_n \cdot \frac{4 R - x_n^3}{3 R}$
> [!success]
> So our answer is $$x_{n+1} = x_n \cdot \frac{4 R - x_n^3}{3 R}$$

- **Restriction:** Since the derivative $b' (x) = -3/x^4$ is undefined at x=0, we must choose an initial guess $x_0\neq 0$. To converge to the positive cube root, choose $x_0>0$.


---
## d. $d(x) = x - R/x^2$
- First, for Newton's method, we need the derivative
	- $d'(x) = 1 + 2R/x^3$
- Using the formula
	- $x_ {n+1} = x_n - \frac{d(x_n)}{d'(x_n)}$ 
	- $= x_n - \frac{x_n - R/x_n^2}{1 + 2R/x_n^3}$
	- $= x_n - \frac{x_n^3 - R/x_n^2 \cdot x_n^3}{x_n^3 + 2R}$
	-  $= x_n - \frac{x_n^4 - R}{x_n^3 + 2R} = x_n - \frac{x_n(x_n^3 - R)}{x_n^3 + 2R}$
	-  $= \frac{x_n(x_n^3 + 2R) - x_n(x_n^3 - R)}{x_n^3 + 2R} = \frac{x_n(x_n^3 + 2R + R - x_n^3)}{x_n^3 + 2R}$
	- = $\frac{x_n(3R)}{x_n^3 + 2R}$
	- = $\frac{3Rx_n}{x_n^3 + 2R}​​$
> [!success]
> Our formula is $X_{n+1} = \frac{3 R x_n}{x_n^3 + 2 R}$
> **Restrictions:**$(x_0 > 0)$.

---
# 14. Determine the formulas for Newton’s method for finding a root of the function $f(x) = x - e^{x/l}$ . What is the behavior of the iterates?
### Getting the formula
- First, get the derivative
	- $f' (x) = 1 - \frac{1}{l}e^{x/l}$
- The Newton’s iteration:
	- $x_{n+1} = x_n - \frac{f (x_n)}{f' (x_n)}$
	- $= x_n - \frac{x_n - e^{x_n/l}}{\, 1-\frac{1}{l}e^{x_n/l}\,}$
> [!success]
> So, our formula is ${x_{n+1} = x_n - \frac{x_n - e^{x_n/l}}{\, 1-\frac{1}{l}e^{x_n/l}\,}}$.


- **Behavior of the Iterates:**
    - For (l > e), two roots exist.
    - Convergence depends on ($x_0$). For ($l \leq e$), iterates might diverge

---

# 18. Determine Newton’s iteration formula for computing the cube root of $N/M$ for nonzero integers $N$ and $M$.
To compute the cube root of NM\frac{N}{M} (with NN and MM nonzero integers), we solve
$f (x)= x^3 - \frac{N}{M}=0$,

So that
$f'(x)= 3 x^2$

Newton’s iteration is:
- $X_{n+1} = x_n - \frac{x_n^3-\frac{N}{M}}{3 x_n^2}$
- $=\frac{3 x_n^3-(x_n^3-\frac{N}{M})}{3 x_n^2}$
- $=\frac{2 x_n^3+\frac{N}{M}}{3 x_n^2}$
- Rearranged this to be  $\frac{2}{3}\, x_n + \frac{N}{3 M\, x_n^2}$.
> [!success]
> $${x_{n+1} = \frac{2}{3}\, x_n + \frac{N}{3 M\, x_n^2}}$$

---
# 25. Newton’s method for finding $\sqrt{R}$ is $x_{n+1} = \frac{1}{2} \left(x_n + \frac{R}{x_n} \right)$. Perform three iterations of this scheme for computing $\sqrt{2}$, starting with $x_0 = 1$, and of the bisection method for $\sqrt{2}$, starting with interval $[1, 2]$. How many iterations are needed for each method in order to obtain $10^{-6}$ accuracy?

### Newton’s Method
Starting with x_0 = 1.
- First iteration; 
	- $X_1 = \frac{1}{2}\Bigl (1+\frac{2}{1}\Bigr)$
	- $= \frac{1}{2}(3)$
	- = 1.5
- Iteration 2: 
	- $X_2 = \frac{1}{2}\Bigl (1.5+\frac{2}{1.5}\Bigr)$
	- $= \frac{1}{2}\Bigl (1.5+1.33333\Bigr)$ 
	- $\approx \frac{2.83333}{2}$
	- = 1.41667
- Iteration 3: 
	- $X_3 = \frac{1}{2}\Bigl (1.41667+\frac{2}{1.41667}\Bigr)$.
	- Since $\frac{2}{1.41667}\approx 1.41176$,
	- then $X_3\approx \frac{1.41667+1.41176}{2}$
	- = 1.414215$.
- Iteration 4:  
	This one will produce an answer accurate to better than $10^{-6}$. The error will be on the order of $10^{-9}$. A lot better that what i need.

> [!success]
> So, we need about of Newton’s method to guarantee an accuracy of $10^{-6}$.

---
### Bisection Method
Interval \([1, 2]\), each iteration halves the error.

The bisection method for $\sqrt{2}$ starts with the interval [1,2][1, 2]. At each step the error (half the interval length) is reduced by a factor of 2.
So, ill use logarithms,
- $N > \log_2 (10^6)$
- $\approx 6\log_2 (10)$
- $\approx 6 (3.32193)$
- $\approx 19.93$
> [!success]
> So, we need at least **20 iterations** to get an accuracy of $10^{-6}$.
