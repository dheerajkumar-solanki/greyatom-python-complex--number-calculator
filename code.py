# --------------
import pandas as pd
import numpy as np
import math

class complex_numbers:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __repr__(self):

        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs(self.imag))
    
    def __add__(self, other):
        real_part = self.real + other.real 
        imag_part = self.imag + other.imag
        return complex_numbers(real_part, imag_part)
    
    def __sub__(self, other):
        real_part = self.real - other.real 
        imag_part = self.imag - other.imag
        return complex_numbers(real_part, imag_part)
    

    def __mul__(self, other):
        if isinstance(other, int):
            real_part = self.real * other.real
            imag_part = self.imag * other.real 
        else:
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.imag * other.real + self.real * other.imag 
        return complex_numbers(real_part, imag_part)
    
    def absolute(self):
        return math.sqrt(self.real**2 + self.imag**2)

    def argument(self):
        return math.atan(self.imag/self.real) * (180/math.pi)

    def conjugate(self):
        return complex_numbers(self.real, -self.imag)

    def __truediv__(self, other):
        den = 1 / (other.real**2 + other.imag**2 )
        return (self * other.conjugate()) * den



    
comp_1 = complex_numbers(3,5)
comp_2 = complex_numbers(4,4)

comp_sum = comp_1 + comp_2
comp_diff = comp_1 - comp_2
comp_prod = comp_1 * comp_2
comp_quot = comp_1 / comp_2
comp_abs = comp_1.absolute()
comp_conj = comp_1.conjugate()
comp_arg = comp_1.argument()
print(comp_arg)

#Code starts here



