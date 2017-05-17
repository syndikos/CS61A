def gcd(a, b):
    """
    a, b: two integers
    returns the greatest common divisor of a and b.
    """
    if b == 0:
        return a
    return gcd(b, a%b)