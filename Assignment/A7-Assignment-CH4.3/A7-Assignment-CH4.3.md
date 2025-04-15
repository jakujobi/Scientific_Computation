# John Akujobi
Section 4.3:  3,  5, and 8.b due on 3/31/2025 10:50 AM
## 3. Derive the approximation formula: $f'(x) \approx \frac{1}{2h} \left[4f(x+h) - 3f(x) - f(x+2h)\right]$
- **Goal:** Derive  
    $f'(x) \approx \frac{1}{2h}\left[4f(x+h)-3f(x)-f(x+2h)\right]$
    
- **Expand $f(x+h)$ and $f(x+2h)$ using Taylor series:**
    - For $f(x+h)$:
        - $f(x+h) = f(x) + h,f'(x) + \frac{h^2}{2},f''(x) + \frac{h^3}{6},f'''(x) + \mathcal{O}(h^4)$
	- For $f(x+2h)$:
	    - $f(x+2h) = f(x) + 2h,f'(x) + 2h^2,f''(x) + \frac{4h^3}{3},f'''(x) + \mathcal{O}(h^4)$
        
- **Substitute into the formula:**
    
    - Write the expression:  
        $4f(x+h) - 3f(x) - f(x+2h)$
        
    - Substitute the series expansions:  
        $4\left(f(x) + h,f'(x) + \frac{h^2}{2},f''(x) + \cdots\right) - 3f(x) - \left(f(x) + 2h,f'(x) + 2h^2,f''(x) + \cdots\right)$
        
- **Simplify term-by-term:**
    - **$f(x)$ - terms:**  
        $4f(x)-3f(x)-f(x)=0$
    - **$f'(x)$ -terms:**  
        $4h,f'(x)-2h,f'(x)=2h,f'(x)$

    - **Higher-order terms:**  
        The leading higher-order term is $-\frac{2h^3}{3},f'''(x)+\mathcal{O}(h^4)$
        
- **Divide both sides by $2h$:**
    - $\frac{1}{2h}\left[4f(x+h)-3f(x)-f(x+2h)\right] = f'(x)-\frac{h^2}{3},f'''(x)+\mathcal{O}(h^3)$
- **Result:**  
    The approximation formula is proportional to an error of $\mathcal{O}(h^2)$.


---

## 5. Averaging the forward-difference formula:  $f'(x) \approx \frac{f(x+h) - f(x)}{h}$ and the backward-difference formula:  $f'(x) \approx \frac{f(x) - f(x-h)}{h}$ Each with error term $O(h)$, results in the central-difference formula:  $f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}$ with error $O(h^2)$. Show why.
**Hint:** Determine at least the first term in the error series for each formula.

- **Forward Difference (FD):**
    - $\frac{f(x+h)-f(x)}{h} = f'(x)+\frac{h}{2},f''(x)+\mathcal{O}(h^2)$
        
- **Backward Difference (BD):**
    - $\frac{f(x)-f(x-h)}{h} = f'(x)-\frac{h}{2},f''(x)+\mathcal{O}(h^2)$
        
- **Average FD and BD:**
    - Compute the average:  
        $\frac{1}{2}\left(\frac{f(x+h)-f(x)}{h}+\frac{f(x)-f(x-h)}{h}\right) = \frac{f(x+h)-f(x-h)}{2h}$
        
- **Error Analysis:**
    - FD error term: $+\frac{h}{2},f''(x)$
    - BD error term: $-\frac{h}{2},f''(x)$
    - Averaging cancels the $\mathcal{O}(h)$ terms, yielding:  
        $\frac{f(x+h)-f(x-h)}{2h}=f'(x)+\frac{h^2}{6},f'''(x)+\mathcal{O}(h^3)$
- **Result:**
	- The central-difference formula  $\displaystyle f'(x) \approx \frac{f(x+h)-f(x-h)}{2h}$  has an error of $\mathcal{O}(h^2)$.
	- The forward and backward formulas both have $O(h)$ error, but their $f'''(x)$ terms are of opposite sign.  
	- When averaged, the first-order error cancels, resulting in a central-difference formula with improved accuracy.

---

## 8.b. Derive the formula $f''(x) \approx \frac{1}{4h^2}\left[f(x+2h) - 2f(x) + f(x-2h)\right]$ and establish formulas for the errors in using them.

- **Goal:** Derive  
    $f''(x) \approx \frac{1}{4h^2}\left[f(x+2h)-2f(x)+f(x-2h)\right]$
    
- **First of, lets expand $f(x+2h)$ and $f(x-2h)$:**
    - $f(x+2h)=f(x)+2h,f'(x)+2h^2,f''(x)+\frac{4h^3}{3},f'''(x)+\frac{2h^4}{3},f''''(x)+\mathcal{O}(h^5)$
    - $f(x-2h)=f(x)-2h,f'(x)+2h^2,f''(x)-\frac{4h^3}{3},f'''(x)+\frac{2h^4}{3},f''''(x)+\mathcal{O}(h^5)$
- **Combine the expansions:**
    - Add the two:  
        $f(x+2h)+f(x-2h)=2f(x)+4h^2,f''(x)+\frac{4h^4}{3},f''''(x)+\mathcal{O}(h^5)$
        
- **Subtract $2f(x)$ and divide by $4h^2$:**
    - $\frac{f(x+2h)-2f(x)+f(x-2h)}{4h^2}=f''(x)+\frac{h^2}{3},f''''(x)+\mathcal{O}(h^3)$
- **Error Term:**  
    The leading error is $\frac{h^2}{3},f''''(x)$, so the formula has an error of $\mathcal{O}(h^2)$.
    
