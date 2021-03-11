def gcd(a, b):
    if (a == 0):
        return b;
    return gcd(b % a, a);

def lowest(den3, num3):
    # Finding gcd of both terms
    common_factor = gcd(num3, den3);
    # Converting both terms
    # into simpler terms by
    # dividing them by common factor
    den3 = int(den3 / common_factor);
    num3 = int(num3 / common_factor);
    print(num3, "/", den3);

def multi_fraction(num1,denom1,num2,denom2):
    denom3 = gcd(denom1, denom2)
    denom3 = (denom1 * denom2)/denom3
    num3 = ((num1) * (denom3 / denom1) * (num2) * (denom3 / denom2))
    return lowest(denom3, num3);

num1 = 1
den1 = 2
num2 = 1
den2 = 2

print(num1, "/", den1, " * ", num2, "/", den2, " is equal to ", end="")
multi_fraction(num1, den1, num2, den2)