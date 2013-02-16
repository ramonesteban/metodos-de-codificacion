def matching(text, pattern):
    counter = 0
    positions = list()
    for i in range(len(text) - len(pattern) + 1):
        section = ''
        for j in range(len(pattern)):
            section += text[i+j]
        if section == pattern:
            counter += 1
            positions.append(i)
    return positions, counter

def main():
    text = 'aababaabababbabbabababaabbababababaabbababbababba'
    pattern = 'abba'
    positions, counter = matching(text, pattern)
    print 'Positions', positions
    print 'Total', counter

if __name__ == '__main__':
    main()

