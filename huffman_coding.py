def frequency_dictionary(text):
    dictionary = dict()
    for i in range(len(text)):
        if dictionary.has_key(text[i]):
            dictionary[text[i]] += 1
        else:
            dictionary[text[i]] = 1
    return dictionary

class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        self.father = None
        self.bit = None

def create_tree(dictionary):
    dictionary = sorted(dictionary.iteritems(), key=lambda value: value[1])
    nodes = list()
    for char, freq in dictionary:
        nodes.append(Node(char, freq))

    while len(nodes) > 1:
        node1 = nodes[0]
        del nodes[0]
        node2 = nodes[0]
        del nodes[0]

        sum_freq = node1.freq + node2.freq
        sum_char = node1.char + node2.char
        father = Node(sum_char, sum_freq, node1, node2)

        node1.father = father
        node2.father = father

        nodes.append(father)
        nodes = sorted(nodes, key=lambda value: value.freq)
    return father

def get_codes(code, node, bits):
    if len(node.char) != 1:
        get_codes(code, node.left, bits + '1')
        get_codes(code, node.right, bits + '0')
    else:
        code = bits
        codes[node.char] = code
        fordecodes[code] = node.char

def encoding(text, codes):
    binary = ''
    f = file('bytes.bin', 'wb')
    for c in text:
        binary += codes[c]
    f.write('%s' % binary)
    print 'Text in binary:', binary
    f.close()
    return len(binary)

def decoding(codes, large):
    f = file('bytes.bin', 'rb')
    bits = f.read(large)
    tmp = ''
    decode_text = ''
    for bit in bits:
        tmp += bit
        if fordecodes.has_key(tmp):
            decode_text += fordecodes[tmp]
            tmp = ''
    f.close()
    return decode_text

def main():
    text = 'today is a good day'
    dictionary = frequency_dictionary(text)
    print 'Frequency:', dictionary
    tree = create_tree(dictionary)
    get_codes('', tree, '')
    print 'Codes:', codes
    print 'Text:', text
    large = encoding(text, codes)
    decode_text = decoding(codes, large)
    print 'Text decoded:', decode_text

if __name__ == '__main__':
    codes = dict()
    fordecodes = dict()
    main()

