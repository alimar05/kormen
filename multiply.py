def multiply(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        m = max(len(str(x)), len(str(x)))
        n = m // 2
                
        a, b = x // 10**n, x % 10**n
        c, d = y // 10**n, y % 10**n

        ac = multiply(a, c)
        ad = multiply(a, d)
        bc = multiply(b, c)
        bd = multiply(b, d)

        return 10**(2*n) * ac + (10**n) * (ad+bc) + bd
    
print(multiply(12334536363348956348756983456389652369587264, 5670234865789324659873456875446464564568))