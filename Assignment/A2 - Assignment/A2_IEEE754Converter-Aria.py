# A2_IEEE754Converter.py
# Author: John Akujobi
# GitHub: https://github.com/jakujobi/
# Date: 2024-02-01
# Version: 1.0


"""
A class to convert decimal (floating-point) numbers to their IEEE-754 representations.

Supports both single precision (32-bit) and double precision (64-bit).

IEEE-754 Format Summary:

- Single Precision (32-bit):
    - 1 sign bit
    - 8 exponent bits with bias 127
    - 23 fraction (mantissa) bits
    
- Double Precision (64-bit):
    - 1 sign bit
    - 11 exponent bits with bias 1023
    - 52 fraction (mantissa) bits

Handles:
    - Normalized numbers,
    - Subnormal numbers,
    - Zeros (with signed zeros),
    - Infinities, and
    - NaN (Not a Number).
"""

import math
from typing import Dict, Any

class IEEE754Converter:
    def to_single(self, value: float) -> Dict[str, Any]:
        """
        Convert a number to its IEEE-754 single precision (32-bit) representation.
        
        Parameters:
            value (float): The number to convert.
            
        Returns:
            dict: Dictionary with keys:
                - 'sign': The sign bit.
                - 'exponent': The stored exponent.
                - 'fraction': The fraction field.
                - 'bit_pattern': The complete 32-bit integer bit pattern.
                - 'binary_str': 32-character string representing the bits.
                - 'hex': Hexadecimal representation.
        """
        total_bits = 32
        exp_bits = 8
        frac_bits = 23
        bias = 127
        return self._float_to_ieee(value, total_bits, exp_bits, frac_bits, bias)
    
    def to_double(self, value: float) -> Dict[str, Any]:
        """
        Convert a number to its IEEE-754 double precision (64-bit) representation.
        
        Parameters:
            value (float): The number to convert.
            
        Returns:
            dict: Dictionary with keys:
                - 'sign': The sign bit.
                - 'exponent': The stored exponent.
                - 'fraction': The fraction field.
                - 'bit_pattern': The complete 64-bit integer bit pattern.
                - 'binary_str': 64-character string representing the bits.
                - 'hex': Hexadecimal representation.
        """
        total_bits = 64
        exp_bits = 11
        frac_bits = 52
        bias = 1023
        return self._float_to_ieee(value, total_bits, exp_bits, frac_bits, bias)
    
    def _float_to_ieee(self, value: float, total_bits: int, exp_bits: int, frac_bits: int, bias: int) -> Dict[str, Any]:
        """
        Convert a float to its IEEE-754 representation based on provided precision.
        
        Parameters:
            value (float): The input number.
            total_bits (int): Total bits (32 or 64).
            exp_bits (int): Number of exponent bits.
            frac_bits (int): Number of fraction bits.
            bias (int): Exponent bias.
        
        Returns:
            dict: Dictionary with keys 'sign', 'exponent', 'fraction', 'bit_pattern',
                  'binary_str', and 'hex'.
        """
        # Determine sign bit.
        sign = 0 if math.copysign(1.0, value) >= 0 else 1

        # Handle special cases.
        if value == 0.0:
            exponent = 0
            fraction = 0
        elif math.isinf(value):
            exponent = (1 << exp_bits) - 1
            fraction = 0
        elif math.isnan(value):
            exponent = (1 << exp_bits) - 1
            fraction = 1 << (frac_bits - 1)  # Quiet NaN.
        else:
            abs_value = abs(value)
            m, exp_raw = math.frexp(abs_value)
            # Normalize mantissa: m in [0.5, 1) -> [1.0, 2.0)
            mantissa = m * 2
            e = exp_raw - 1  # Adjust exponent because we scaled m.

            if e + bias <= 0:
                # Subnormal number.
                exponent = 0
                # Scale abs_value so that effective exponent is 1-bias.
                fraction = int(round(abs_value / (2 ** (1 - bias)) * (2 ** frac_bits)))
                if fraction >= (1 << frac_bits):
                    fraction = (1 << frac_bits) - 1
            else:
                stored_exp = e + bias
                frac_part = mantissa - 1.0  # Remove the implicit bit.
                fraction = int(round(frac_part * (2 ** frac_bits)))
                # Rounding overflow: adjust exponent.
                if fraction == (1 << frac_bits):
                    stored_exp += 1
                    fraction = 0
                if stored_exp >= (1 << exp_bits) - 1:
                    # Overflow: set to infinity.
                    stored_exp = (1 << exp_bits) - 1
                    fraction = 0
                exponent = stored_exp

        # Assemble bit pattern.
        if total_bits == 32:
            bit_pattern = (sign << 31) | (exponent << frac_bits) | fraction
        elif total_bits == 64:
            bit_pattern = (sign << 63) | (exponent << frac_bits) | fraction
        else:
            fraction_bits = total_bits - 1 - exp_bits
            bit_pattern = (sign << (total_bits - 1)) | (exponent << fraction_bits) | fraction

        binary_str = format(bit_pattern, f'0{total_bits}b')
        hex_str = hex(bit_pattern)
        
        return {
            'sign': sign,
            'exponent': exponent,
            'fraction': fraction,
            'bit_pattern': bit_pattern,
            'binary_str': binary_str,
            'hex': hex_str
        }



# -------------------------
# Using it to attempt my MATH 374 2nd Homework
# -------------------------
def main():
    converter = IEEE754Converter()
    
    test_values = [
        ("+1.0", 1.0),
        ("-1.0", -1.0),
        ("+0.0", 0.0),
        ("-0.0", -0.0),
        ("-9876.54321", -9876.54321),
        ("64.37109375", 64.37109375)
    ]
    
    for label, value in test_values:
        print(f"Value: {label} ({value})")
        
        # Single Precision.
        single = converter.to_single(value)
        print(" Single Precision (32-bit):")
        print(f"  Binary:   {single['binary_str']}")
        print(f"  Hex:      {single['hex']}")
        print(f"  Fields:   Sign = {single['sign']}  Exponent = {single['exponent']}  Fraction = {single['fraction']}")
        print("")
        
        # Double Precision.
        double = converter.to_double(value)
        print(" Double Precision (64-bit):")
        print(f"  Binary:   {double['binary_str']}")
        print(f"  Hex:      {double['hex']}")
        print(f"  Fields:   Sign = {double['sign']}  Exponent = {double['exponent']}  Fraction = {double['fraction']}")
        print("\n" + "=" * 60 + "\n")

if __name__ == '__main__':
    main()

