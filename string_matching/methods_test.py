import sys, time, random

def naive(pattern, text):
    # Used variables:
    # m - length of the pattern
    # n - length of the text

    matches_positions = list()
    comparations = 0

    m = len(pattern)
    n = len(text)

    start = time.time()
    for i in range(n - m + 1):
        section = ''
        for j in range(m):
            section += text[i+j]
            comparations += 1
        if section == pattern:
            matches_positions.append(i)
    end = time.time()
    runtime = end - start
    return matches_positions, runtime, comparations

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

    start = time.time()
    while k <= n:
        i = m
        h = k
        while i > 0 and pattern[i-1] == text[h-1]:
            comparations += 1
            i -= 1
            h -= 1
        if i == 0:
            matches_positions.append(k - m)
            k += 1
        else:
            k += bad_character[text[h-1]]
    end = time.time()
    runtime = end - start
    return matches_positions, runtime, comparations

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

def knuth_morris_pratt(pattern, text):
    # Used variables:
    # m - length of the pattern
    # n - length of the text
    # p - current position of the pattern
    # c - current position of the text

    table = kmp_table(pattern)
    matches_positions = list()
    comparations = 0

    m = len(pattern)
    n = len(text)
    p = 0
    c = 0

    start = time.time()
    while p + c < n:
        if pattern[p] == text[c + p]:
            comparations += 1
            if p == m - 1:
                matches_positions.append(c)
                c += 1
                p = 0
            else:
                p += 1
        else:
            c = c + p - table[p]
            if table[p] > -1:
                p = table[p]
            else:
                p = 0

    end = time.time()
    runtime = end - start
    return matches_positions, runtime, comparations

def kmp_table(pattern):
    table = list()
    m = len(pattern)

    for i in range(m):
        table.append(0)
    table[0] = -1
    table[1] = 0

    position = 2
    candidate = 0
    while position < m:
        if pattern[position-1] == pattern[candidate]:
            candidate += 1
            table[position] = candidate
            position += 1
        elif candidate > 0:
            candidate = table[candidate]
        else:
            table[position] = 0
            position += 1
    return table

def instance_generator(pattern_len, text_len):
    letters_set = map(chr, range(97, 123))
    random.shuffle(letters_set)
    letters_subset = letters_set[:5]

    pattern = ''
    text = ''
    length = 0

    for i in range(pattern_len):
        pattern += letters_subset[int(random.uniform(0, 5))]

    while length < text_len:
        if random.random() < 0.2 and length < (text_len - pattern_len):
            text += pattern
            length += pattern_len
        else:
            text += letters_subset[int(random.uniform(0, 5))]
            length += 1
    return pattern, text

def main():
    pattern, text = instance_generator(int(sys.argv[1]), int(sys.argv[2]))
    print pattern, text

    matches_positions, runtime, comparations = naive(pattern, text)
    print 'naive', matches_positions, runtime, comparations

    matches_positions, runtime, comparations = boyer_moore(pattern, text)
    print 'bm   ', matches_positions, runtime, comparations

    matches_positions, runtime, comparations = knuth_morris_pratt(pattern, text)
    print 'kmp  ', matches_positions, runtime, comparations

if __name__ == '__main__':
    main()

