def naive(pattern, text):
    # Used variables:
    # m - length of the pattern
    # n - length of the text

    matches_positions = list()
    comparations = 0

    m = len(pattern)
    n = len(text)

    for i in range(n - m + 1):
        section = ''
        for j in range(m):
            section += text[i+j]
            comparations += 1
        if section == pattern:
            matches_positions.append(i)
    return matches_positions, comparations

def main():
    pattern = 'abba'
    text = 'abbabababbaaababbabbbabbabbabbaabbbabaabba'
    matches_positions, comparations = naive(pattern, text)
    print 'Matching positions', matches_positions
    print 'Total matches', len(matches_positions)
    print 'Comparations', comparations

if __name__ == '__main__':
    main()

