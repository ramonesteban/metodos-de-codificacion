def boyer_moore(pattern, text):
    # Used variables:
    # m - length of the pattern
    # n - length of the text
    # k - first position of the character to compare
    # i - current position of the pattern
    # h - current position of the text

    bad_character = bad_character_rule(pattern, text)
    matches_positions = list()
    comparations = 0

    m = len(pattern)
    n = len(text)
    k = m

    while k <= n:
        i = m
        h = k
        while i > 0 and pattern[i-1] == text[h-1]:
            comparations += 1
            i -= 1
            h -= 1
        if i == 0:
            matches_positions.append(k - m)
        k += bad_character[text[h-1]]
    return matches_positions, comparations

def bad_character_rule(pattern, text):
    m = len(pattern)
    n = len(text)
    bad_character = {}

    for i in range(n - 1):
        if text[i] not in pattern:
            bad_character[text[i]] = m
    for i in range(m - 1):
        bad_character[pattern[i]] = m - 1 - i
    return bad_character

def main():
    pattern = 'abba'
    text = 'abbabababbaaababbabbbabbabbabbaabbbabaabba'
    matches_positions, comparations = boyer_moore(pattern, text)
    print 'Matching positions', matches_positions
    print 'Total matches', len(matches_positions)
    print 'Comparations', comparations

if __name__ == '__main__':
    main()

