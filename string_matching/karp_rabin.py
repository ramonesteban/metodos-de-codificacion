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

def karp_rabin(P, T):
    n = len(P)
    m = len(T)
    hash_P = definition1(P, n)
    matching_positions = list()

    for r in range(m-n+1):
        hash_T = definition2(T, n, r)
        if hash_P == hash_T:
            matching_positions.append(r)

    print 'Matching positions', matching_positions

def main():
    P = '111'
    T = '00011100000111110001100111'
    karp_rabin(P, T)

if __name__ == '__main__':
    main()

