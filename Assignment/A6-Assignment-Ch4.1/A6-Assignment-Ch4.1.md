Section 4.1:  6, 7.b, and 10.a due

---

# 6. Find the polynomial $p$ of least degree that takes these values:  
- $p(0) = 2$
- $p(2) = 4$
- $p(3) = -4$
- $p(5) = 82$
Use divided differences to get the correct polynomial. It is _not_ necessary to write the polynomial in the standard form $a_0 + a_1 x + a_2 x^2 + \cdots$.
### Theory Recap
- **Divided differences** provide a way to recursively compute the coefficients of the interpolation polynomial.
- The **Newton form** of the interpolation polynomial is:
    - $p(x)= f[x_0] + f[x_0,x_1](x-x_0) + f[x_0,x_1,x_2](x-x_0)(x-x_1) + \cdots$

### Working Steps
- **Step 1. List the data points:**
    - $x_0 = 0$,  $f(x_0)=2$
    - $x_1 = 2$,  $f(x_1)=4$
    - $x_2 = 3$,  $f(x_2)=-4$
    - $x_3 = 5$,  $f(x_3)=82$

- **Step 2. Calc the first divided differences:**
    - $f[x_0,x_1] = \frac{f(x_1)-f(x_0)}{x_1-x_0} = \frac{4-2}{2-0} = \frac{2}{2} = 1$
    - $f[x_1,x_2] = \frac{f(x_2)-f(x_1)}{x_2-x_1} = \frac{-4-4}{3-2} = \frac{-8}{1} = -8$
    - $f[x_2,x_3] = \frac{f(x_3)-f(x_2)}{x_3-x_2} = \frac{82-(-4)}{5-3} = \frac{86}{2} = 43$

- **Step 3. Calc the second divided differences:**
    - $f[x_0,x_1,x_2] = \frac{f[x_1,x_2]-f[x_0,x_1]}{x_2-x_0} = \frac{-8-1}{3-0} = \frac{-9}{3} = -3$
    - $f[x_1,x_2,x_3] = \frac{f[x_2,x_3]-f[x_1,x_2]}{x_3-x_1} = \frac{43-(-8)}{5-2} = \frac{51}{3} = 17$

- **Step 4. Calc the third divided difference:**
    - $f[x_0,x_1,x_2,x_3] = \frac{f[x_1,x_2,x_3]-f[x_0,x_1,x_2]}{x_3-x_0} = \frac{17-(-3)}{5-0} = \frac{20}{5} = 4$

- **Step 5. Write the Newton interpolation polynomial:**
    - The general form is:
        - $p(x)= f[x_0] + f[x_0,x_1](x-x_0) + f[x_0,x_1,x_2](x-x_0)(x-x_1) + f[x_0,x_1,x_2,x_3](x-x_0)(x-x_1)(x-x_2)$
    - Substituting the computed values:
        - $p(x)= 2 + 1\,(x-0) - 3\,(x-0)(x-2) + 4\,(x-0)(x-2)(x-3)$

- **Final Answer for Problem 6:**
    - $p(x)= 2 + x - 3(x)(x-2) + 4(x)(x-2)(x-3)$

### Divided Difference Table

| $x$ | $f[,]$ | $f[, , ,]$ | $f[, , , , ,]$ | $f[, , , , , , ,]$ |
|---|---|---|---|---|
|0|2||||
|2|4|1|||
|3|-4|-8|-3||
|5|82|43|17|4|


---

# 7.b.
Complete the following divided-difference tables, and use them to obtain polynomials of degree 3 that interpolate the function values indicated:

|$x$|$f[\ ]$|$f[\ ,\ ]$|$f[\ ,\ ,\ ]$|$f[\ ,\ ,\ ,\ ]$|
|---|---|---|---|---|
|$-1$|$2$||||
|$1$|$-4$||||
|$3$|$46$|$53.5$|||
|$4$|$99.5$||||

Write the final polynomials in a form most efficient for computing.


### Theory Recap
- As before, the Newton form is:
    - $p(x)= f[x_0] + f[x_0,x_1](x-x_0) + f[x_0,x_1,x_2](x-x_0)(x-x_1) + f[x_0,x_1,x_2,x_3](x-x_0)(x-x_1)(x-x_2)$
- Each level of divided differences is computed using:
    - $f[x_i,x_{i+1},\dots,x_{i+k}] = \frac{f[x_{i+1},\dots,x_{i+k}] - f[x_i,\dots,x_{i+k-1}]}{x_{i+k} - x_i}$

### Working Steps
- **Step 1. List the data points:**
    - $x_0 = -1$, \quad $f(x_0)=2$
    - $x_1 = 1$, \quad $f(x_1)=-4$
    - $x_2 = 3$, \quad $f(x_2)=46$
    - $x_3 = 4$, \quad $f(x_3)=99.5$

- **Step 2. Calc the first divided differences:**
    - $f[x_0,x_1] = \frac{-4-2}{1-(-1)} = \frac{-6}{2} = -3$
    - $f[x_1,x_2] = \frac{46-(-4)}{3-1} = \frac{50}{2} = 25$
    - $f[x_2,x_3] = \frac{99.5-46}{4-3} = \frac{53.5}{1} = 53.5$
        - (Note: The table already gives $f[x_2,x_3] = 53.5$)

- **Step 3. Calc the second divided differences:**
    - $f[x_0,x_1,x_2] = \frac{25 - (-3)}{3 - (-1)} = \frac{28}{4} = 7$
    - $f[x_1,x_2,x_3] = \frac{53.5 - 25}{4 - 1} = \frac{28.5}{3} = 9.5$

- **Step 4. Calc the third divided difference:**
    - $f[x_0,x_1,x_2,x_3] = \frac{9.5 - 7}{4 - (-1)} = \frac{2.5}{5} = 0.5$

- **Step 5. Write the Newton interpolation polynomial:**
    - Using $x_0=-1$, the polynomial is:
        - $p(x)= f[x_0] + f[x_0,x_1](x-(-1)) + f[x_0,x_1,x_2](x-(-1))(x-1) + f[x_0,x_1,x_2,x_3](x-(-1))(x-1)(x-3)$
    - Substitute the values:
        - $p(x)= 2 - 3\,(x+1) + 7\,(x+1)(x-1) + 0.5\,(x+1)(x-1)(x-3)$

- **Final Answer for Problem 7 (b):**
    - $p(x)= 2 - 3(x+1) + 7(x+1)(x-1) + 0.5(x+1)(x-1)(x-3)$

### Completed Divided Difference Table

| $x$ | $f[,]$ | $f[, , ,]$ | $f[, , , , ,]$ | $f[, , , , , , ,]$ |
|---|---|---|---|---|
|-1|2|-3|7|0.5|
|1|-4|25|9.5||
|3|46|53.5|||
|4|99.5||||


---

# 10.a. Construct Newton’s interpolation polynomial for the data shown.

|$x$|$0$|$2$|$3$|$4$|
|---|---|---|---|---|
|$y$|$7$|$11$|$28$|$63$|

### Theory Recap
- The Newton interpolation polynomial is built as:
    - $p(x)= f[x_0] + f[x_0,x_1](x-x_0) + f[x_0,x_1,x_2](x-x_0)(x-x_1) + f[x_0,x_1,x_2,x_3](x-x_0)(x-x_1)(x-x_2)$
- This method uses the computed divided differences to progressively build the polynomial.

### Working Steps
- **Step 1. List the data points:**
    - $x_0 = 0$,  $f(x_0)=7$
    - $x_1 = 2$,  $f(x_1)=11$
    - $x_2 = 3$,  $f(x_2)=28$
    - $x_3 = 4$,  $f(x_3)=63$

- **Step 2. Calc the first divided differences:**
    - $f[x_0,x_1] = \frac{11-7}{2-0} = \frac{4}{2} = 2$
    - $f[x_1,x_2] = \frac{28-11}{3-2} = \frac{17}{1} = 17$
    - $f[x_2,x_3] = \frac{63-28}{4-3} = \frac{35}{1} = 35$

- **Step 3. Calc the second divided differences:**
    - $f[x_0,x_1,x_2] = \frac{17-2}{3-0} = \frac{15}{3} = 5$
    - $f[x_1,x_2,x_3] = \frac{35-17}{4-2} = \frac{18}{2} = 9$

- **Step 4. Calc the third divided difference:**
    - $f[x_0,x_1,x_2,x_3] = \frac{9-5}{4-0} = \frac{4}{4} = 1$

- **Step 5. Write the Newton interpolation polynomial:**
    - Since $x_0 = 0$, the polynomial is:
        - $p(x)= f(x_0) + f[x_0,x_1](x-0) + f[x_0,x_1,x_2](x-0)(x-2) + f[x_0,x_1,x_2,x_3](x-0)(x-2)(x-3)$
    - Substitute the values:
        - $p(x)= 7 + 2x + 5x(x-2) + 1\cdot x(x-2)(x-3)$

- **Final Answer for Problem 10 (a):**
    - $p(x)= 7 + 2x + 5x(x-2) + x(x-2)(x-3)$


### Divided Difference Table

| $x$ | $f[,]$ | $f[, , ,]$ | $f[, , , , ,]$ | $f[, , , , , , ,]$ |
| --- | ------ | ---------- | -------------- | ------------------ |
| 0   | 7      | 2          | 5              | 1                  |
| 2   | 11     | 17         | 9              |                    |
| 3   | 28     | 35         |                |                    |
| 4   | 63     |            |                |                    |

### Newton Interpolating Polynomial
- $p (x) = 7 + 2 x + 5 x (x - 2) + x (x - 2)(x - 3)$

---
