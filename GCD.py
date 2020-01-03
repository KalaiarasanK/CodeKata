#Given 2 numbers N,M find the GCD of N and M.If it cannot be found for given number(s) then print -1


def gcd(a, b):
    if a%b == 0:
        return b
    return gcd(b, a%b)
print(gcd(10,5))  
