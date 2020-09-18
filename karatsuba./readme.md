## Karatsuba Fast Multiplication using Divide and Conquer
Given two integers x and y of length n:
1. Compute a and b such that: x = 10<sup>n/2</sup>a + b
2. Compute c and d such that: y = 10<sup>n/2</sup>c + d
3. Compute a*c recursively
4. Compute b*d recursively
5. Compute (a+b) * (c+d) recursively
6. Then a*d + b*c = 5 -4 -3
7. x*y = 10<sup>n</sup> * ac + 10<sup>n/2</sup> * (ad+bc) + bd
