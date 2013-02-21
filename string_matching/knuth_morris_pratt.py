def knuth_morris_pratt(pattern, text):
    # Used variables:
    # m - length of the pattern
    # n - length of the text
    # p - current position of the pattern
    # c - current position of the text

    shift_positions = preprocessing(pattern)
    matches_positions = list()
    comparations = 0

    m = len(pattern)
    n = len(text)
    p = 0
    c = 0

    while c < n:
        if text[c] == pattern[p]:
            comparations += 1
            c += 1
            p += 1
            if p == m:
                matches_positions.append(c - m)
                p = 0
        elif p == 0:
            c += shift_positions[p]
            p = 0
        else:
            c += 1
            p = 0
    return matches_positions, comparations

def preprocessing(pattern):
    shift_positions = list()
    m = len(pattern)

    for i in range(m):
        shift_positions.append(0)
    shift_positions[0] = -1
    shift_positions[1] = 0

    position = 2
    candidate = 0
    while position < m:
        if pattern[position-1] == pattern[candidate]:
            candidate += 1
            shift_positions[position] = candidate
            position += 1
        elif candidate > 0:
            candidate = shift_positions[candidate]
        else:
            shift_positions[position] = 0
            position += 1
    return shift_positions

def main():
    pattern = 'abba'
    text = 'abbabababbaaababbabbbabbabbabbaabbbabaabba'
    matches_positions, comparations = knuth_morris_pratt(pattern, text)
    print 'Matching positions', matches_positions
    print 'Total matches', len(matches_positions)
    print 'Comparations', comparations

if __name__ == '__main__':
    main()

