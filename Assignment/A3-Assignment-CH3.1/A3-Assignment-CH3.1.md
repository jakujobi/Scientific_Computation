# John Akujobi - Math 374 - Spring 2025

> [!info]
> All web searches referenced were done with Perplexity app


---
# 7.
> [!question]
> Prove Inequality (1).
> $$ |r - c_n| \leq \frac{b_0 - a_0}{2^{n+1}} $$

> [!info]
> Information from our Text Book
> If the bisection algorithm is now applied and if the computed quantities are denoted by  
> $a_0, b_0, c_0, a_1, b_1, c_1$, and so on, then by the same reasoning,
> 
> $$
> |r - c_n| \leq \frac{b_n - a_n}{2} \quad (n \geq 0)
> $$
> 
> Since the widths of the intervals are divided by 2 in each step, we conclude that
> 
> $$
> |r - c_n| \leq \frac{b_0 - a_0}{2^{n+1}}
> $$
> 
> To summarize, a theorem can be written as follows:
> Bisection Method Theorem: If the bisection algorithm is applied to a continuous function $f$ on an interval $[a, b]$, where $f(a) f(b) < 0$, then, after $n$ steps, an approximate root will have been computed with error at most: $$ \frac{b - a}{2^{n+1}} $$
> If an error tolerance has been prescribed in advance, it is possible to determine the number of steps required in the bisection method. Suppose that we want: $$ |r - c_n| < \epsilon $$ Then it is necessary to solve the following inequality for $n$: $$ \frac{b - a}{2^{n+1}} < \epsilon $$ By taking logarithms (with any convenient base), we obtain: $$ n > \frac{\log(b - a) - \log(2\epsilon)}{\log 2} $$

### Solution
$$ |r - c_n| \leq \frac{b_0 - a_0}{2^{n+1}} $$

- The bisection method produces a sequence of intervals $[a_n,b_n]$ that contain the root $r$, with the midpoint given by $c_n=\frac{a_n+b_n}{2}$. Since $r$ lies in the interval, we have
$|r-c_n|\le\frac{b_n-a_n}{2}$.

- At each step, the interval length is halved, so we get
	$b_n-a_n=\frac{b_0-a_0}{2^n}$.

- Substituting $b_n - a_n = \frac{b_0 - a_0}{2^n}$  into the error bound gives us
	$|r-c_n|\le\frac{1}{2}\cdot\frac{b_0-a_0}{2^n}=\frac{b_0-a_0}{2^{n+1}}$.

- Sooo, we have proven that
	$|r-c_n|\le\frac{b_0-a_0}{2^{n+1}}$.



---
# 8.
> [!question]
> If $a = 0.1$ and $b = 1.0$, how many steps of the bisection method are needed to determine the root with an error of at most $\frac{1}{2} \times 10^{-8}$?
### Solution
- First, what do i have here:
	- Initial interval: $a=0.1$ and $b=1.0$, so the width is $b-a=0.9$.
	- Error tolerance that we want: $\epsilon=\frac{1}{2}\times10^{-8}$.

- With the bisection method, after $n$ steps the error is bounded by
	$|r-c_n|\le\frac{b_0-a_0}{2^{n+1}}$.

- To guarantee an error of at most $\epsilon$, we require
	$\frac{0.9}{2^{n+1}}\le\frac{1}{2}\times10^{-8}$.

- This inequality can be rearranged as follows:
	1. Multiply both sides by $2^{n+1}$:
	    $0.9\le\frac{1}{2}\times10^{-8}\cdot2^{n+1}$.
	    
	2. Multiply both sides by $2$:
	    $1.8\le10^{-8}\cdot2^{n+1}$.
	    
	3. Rearranging gives:
	    $2^{n+1}\ge\frac{1.8}{10^{-8}}=1.8\times10^8$.

- Taking logarithms (base $2$):
	$n+1\ge\log_2(1.8\times10^8)=\log_2(1.8)+\log_2(10^8)$.

- I remember that:
	- $\log_2(10^8)=8\log_2(10)\approx8\times3.32193\approx26.57544$
	- $\log_2(1.8)\approx0.848$

- Thus,
	$n+1\ge26.57544+0.848\approx27.42344$.

Since $n+1$ must be an integer, we have
	$n+1\ge28$  ⟹ $n\ge27$.


> [!success]
> Soo, we need at least **27 steps**



---

# 14.
> [!question]
>Denote the successive intervals that arise in the bisection method by $[a_0, b_0]$, $[a_1, b_1]$, $[a_2, b_2]$, and so on. Show that 
> - **a.** $a_0 \leq a_1 \leq a_2 \leq \dots$ and $b_0 \geq b_1 \geq b_2 \geq \dots$
> - **b.** $b_n - a_n = 2^{-n} (b_0 - a_0)$
> - **c.** $a_n b_n + a_{n-1} b_{n-1} = a_{n-1} b_n + a_n b_{n-1}$ for all $n$. 
### (a) $a_0 \leq a_1 \leq a_2 \leq \dots$ and $b_0 \geq b_1 \geq b_2 \geq \dots$
> [!info]
> 
Searching online, i found out that this is called the monotonicity of Endpoints

At each step of the bisection method an interval is chosen that is a subinterval of the previous one. That is, if we start with the interval $[a_n,b_n]$ and compute the midpoint $c_n=\frac{a_n+b_n}{2}$, then either
- the new interval is $[a_n,c_n]$, or
- it is $[c_n,b_n]$.

In the first case, the left endpoint remains the same ($a_{n+1}=a_n$) and the right endpoint becomes $c_n$ with $a_n<c_n\le b_n$. In the second case, the right endpoint remains the same ($b_{n+1}=b_n$) and the left endpoint becomes $c_n$ with $a_n\le c_n<b_n$. Thus, in every step we have

$a_n\le a_{n+1}$ and $b_{n+1}\le b_n$.

> [!success]
> This shows that the sequence $a_0,a_1,a_2,\dots$ is non-decreasing and $b_0,b_1,b_2,\dots$ is non-increasing.

---
### (b) $b_n - a_n = 2^{-n} (b_0 - a_0)$
> [!info]
Searching online, i found out that this is called the Length of the Intervals
- The initial interval has length `$b_0-a_0$`. At each step the interval is halved, so that after one step
	$b_1-a_1=\frac{b_0-a_0}{2}$
- By induction, after n steps the length of the interval is
	$b_n-a_n=\frac{b_0-a_0}{2^n}$ .

---
### (c)  $a_n b_n + a_{n-1} b_{n-1} = a_{n-1} b_n + a_n b_{n-1}$ for all $n$. 
> [!info]
Searching online, i found out that this is called the Endpoint Product Identity
- We need to show that for all n
	$A_n b_n+a_{n-1}b_{n-1}=a_{n-1}b_n+a_n b_{n-1}$

- Subtract the right-hand side from the left-hand side:
	$A_n b_n+a_{n-1}b_{n-1}-a_{n-1}b_n-a_n b_{n-1}$

- Group the terms as follows:
	$\bigl(a_n b_n-a_n b_{n-1}\bigr)-\bigl(a_{n-1}b_n-a_{n-1}b_{n-1}\bigr) =a_n(b_n-b_{n-1})-a_{n-1}(b_n-b_{n-1}$).

- Factor out $b_n-b_{n-1}$:
	$(a_n-a_{n-1})(b_n-b_{n-1})$.

- In the bisection method, in each iteration only one endpoint changes (either $a_n=a_{n-1}$ or $b_n=b_{n-1}$), so one of the factors is zero. Hence,
	$(a_n-a_{n-1})(b_n-b_{n-1})=0$,

- Which means
	$A_n b_n+a_{n-1}b_{n-1}=a_{n-1}b_n+a_n b_{n-1}$.



---

# 15.
> [!question]
> (Continuation) Can $a_0 = a_1 = a_2 = \dots$ happen?

I searched online that constant left endpoints are possible.

It happens if at every step the interval selected is of the form $[a_n,c_n]$ instead of $[c_n,b_n]$.
In that case the left endpoint stays the same throughout the iterations (i.e. $a_{n+1}=a_n$ for all n). Here the, function values meet $f(a_n)f(c_n)<0$ at every step, which makes the algorithm to choose the left half of the interval every time.

Soo, constant Left endpoints like a0=a1=a3=.... are possible



---

# 16.
> [!question]
> (Continuation) Let $c_n = (a_n + b_n)/2$. Show that > $$
> \lim_{n \to \infty} c_n = \lim_{n \to \infty} a_n = \lim_{n \to \infty} b_n.
> $$

Define the midpoint $c_n=\frac{a_n+b_n}{2}$. We have already shown that the sequence $a_n$  is non-decreasing and the sequence  $b_n$ is non-increasing. Since each  $a_n$ is bounded above (by any  $b_n$) and each  $b_n$  is bounded below (by any  $a_n$ ), both sequences converge. Denote
	$\lim_{n\to\infty}a_n=\ell_a\quad\text{and}\quad\lim_{n\to\infty}b_n=\ell_b$.

- From part (b) we know
	$B_n-a_n=\frac{b_0-a_0}{2^n}$

- Taking the limit as $n\to\infty$ yields
	$\lim_{n\to\infty}(b_n-a_n)=0$,

- So that
	$\ell_b-\ell_a=0\quad\text{or}\quad \ell_a=\ell_b$

- Since $c_n=\frac{a_n+b_n}{2}$, its limit is
	$lim_{n\to\infty}c_n=\frac{\ell_a+\ell_b}{2}=\ell_a$.

- So, we conclude that
	$\lim_{n\to\infty}c_n=\lim_{n\to\infty}a_n=\lim_{n\to\infty}b_n$.

> [!info]
Searching online, i found out that this is called the Convergence of the Endpoints and Midpoints



---
# 22.
> [!question]
> If the bisection method is applied with starting interval $[2^m, 2^{m+1}]$, where $m$ is a positive or negative integer, how many steps should be taken to compute the root to full machine precision on a 32-bit word-length computer?

### Solution
- We are given a starting interval of the form $[2^m,2^{m+1}]$, where $m$ is any integer. The width of this interval is
	$b_0-a_0=2^{m+1}-2^m=2^m$.

- After $n$ steps, the error bound is
	$|r-c_n|\le\frac{2^m}{2^{n+1}}=2^{m-n-1}$.

- On a 32-bit word-length computer (using IEEE single precision), the number is represented with a 24-bit significand (including the implicit bit). This means that for numbers of magnitude about $2^m$, the spacing between adjacent representable numbers is approximately
	$2^{m-23}$.

- To achieve full machine precision, the error must be no larger than this spacing. Hence, we require
	$2^{m-n-1}\le2^{m-23}$.

- Canceling $2^m$ from both sides yields:
	$2^{-n-1}\le2^{-23}$.

- Taking logarithms (base $2$):
	$-n-1\le-23$ ⟹ $n+1\ge23$ ⟹ $n\ge22$.

> [!success]
> Sooo, we need **22 steps** to compute the root to full machine precision.

---

