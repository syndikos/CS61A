def gcd(a, b):
    """
    a, b: two integers
    returns the greatest common divisor of a and b.
    """
    if b == 0:
        return a
    return gcd(b, a%b)
    


class Cons(object):
    """
    define a rational number with n as its or
    and d as its cdr
    """
    

    def __init__(self, n, d):
        g = gcd(n, d)
        self.car = int(n / g)
        self.cdr = int(d / g)

    def setCar(self, n):
        self.car = n

    def setCdr(self, d):
        self.cdr = d

    def getCar(self):
        return self.car

    def getCdr(self):
        return self.cdr

    def __str__(self):
        return str(self.car) + '/' + str(self.cdr)
    def getSelf(self): 
        return self



class positiveRat(Cons):
    def __init__(self, n, d):
        Cons.__init__(self, n, d)
    def add_rat(self, other):
        numer = self.car * other.cdr + self.cdr * other.car
        denomer = self.cdr * other.cdr
        c = positiveRat(numer, denomer)
        return c

    def sub_rat(self, other):
        numer = self.car * other.cdr - self.cdr * other.car
        denomer = self.cdr * other.cdr
        c = positiveRat(numer, denomer)
        return c

    def mul_rat(self, other):
        numer = self.car * other.car
        denomer = self.cdr * other.cdr
        c = positiveRat(numer, denomer)
        return c


    def div_rat(self, other) :
        numer = self.car * other.cdr
        denomer = self.cdr * other.car
        c = positiveRat(numer, denomer)
        return c


    def equal_rat(self, other):
        numer = self.car * other.cdr
        denomer = self.cdr * other.car
        return numer == denomer

class Rate(positiveRat):
    """
    rational number including all positive and negative numbers
    """
    def __init__(self, n, d):
        positiveRat.__init__(self, n, d)
        g = gcd(n, d)
        
        if n*d  < 0 :
            self.car = -abs(int(n / g))
        else:
            self.car = abs(int(n / g))
        self.cdr = abs(d)




