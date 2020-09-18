# Implementing Karastuba Multiplication
import math
class kartsuba_algo:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def karatsuba(self):
    if self.x < 10 and self.y < 10: # return when both x and y are single digits
        return x * y

    n = max(len(str(self.x)) , len(str(self.y)))
    m = math.ceil(n/2) #to take care of odd n

    a = self.x // (10 ** (m))
    b = self.x % (10 ** (m))
    c = self.y // (10 ** (m))
    d = self.y % (10 ** (m))

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b , c + d) - ac - bd

    return (ac * 10**(2*m) + ad_bc * 10**(m) + bd)


if __name__ == "__main__":

    x = int(input("Please enter the first number: \n"))
    y = int(input("Please enter the second number: \n"))

    xy = karatsuba (x, y)
    xy_true = x*y
    print("product of {} and {} by karatsuba is {} \n".format(x, y, xy))
    if xy == xy_true:
        print("The computed value matches the inbuilt Multiplication routine value")



