def definition1(P, n):
    total_sum = 0

    for i in range(n):
        total_sum += 2**(n-i)*int(P[i])
    return total_sum

def definition2(T, n, r):
    total_sum = 0

    for i in range(n):
        total_sum += 2**(n-i)*int(T[r+i])
    return total_sum

def main():
    P = '1001'
    T = '0101011000101101001'

    n = len(P)
    r = input('r = ')

    print 'H(P) =', definition1(P, n)
    print 'H(Tr) =', definition2(T, n, r)

if __name__ == '__main__':
    main()

