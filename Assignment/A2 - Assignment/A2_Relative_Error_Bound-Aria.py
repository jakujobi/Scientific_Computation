# A2_Relative_Error_Bound.py
# Author: John Akujobi
# GitHub: https://github.com/jakujobi/
# Date: 2024-02-01
# Version: 1.0

def relative_error_bound(beta: float, n: int) -> float:
    return 0.5 * (beta ** (1 - n))


if __name__ == "__main__":
    beta = 10
    n = 4
    bound = relative_error_bound(beta, n)
    print(f"Relative error bound for beta = {beta} and n = {n} is {bound:.6f}")

# A3_Relative_Error_Bound.py Documentation

"""
Calculate the relative error bound in a normalized floating-point system.

For a floating-point system with base `beta` and `n` digits in the mantissa,
the relative error bound (machine epsilon) is given by:
    0.5 * beta^(1 - n)

Parameters:
    beta (float): The base of the floating-point system (e.g., 2 or 10).
    n (int): The number of digits in the mantissa.

Returns:
    float: The computed relative error bound.

Examples:
    >>> relative_error_bound(10, 4)
    0.0005
"""