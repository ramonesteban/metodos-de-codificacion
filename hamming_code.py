import sys, random, numpy

def binary_matrix(matrix):
    for element in numpy.nditer(matrix, op_flags=['readwrite']):
        if element > 1 and element%2 == 0:
            element[...] = 0
        if element > 1 and element%2 != 0:
            element[...] = 1
    return matrix

def get_biterror(matrix):
    matrix = numpy.squeeze(numpy.asarray(matrix))
    matrix = matrix[::-1]
    num = 0
    for i in range(len(matrix)):
        num += matrix[i]*(2**i)
    return int(num)

def recover_correct_code(matrix, biterror):
    matrix = numpy.squeeze(numpy.asarray(matrix))
    for i in range(len(matrix)):
        if i == biterror - 1 and matrix[i] == 0:
            matrix[i] = 1
            break
        if i == biterror - 1 and matrix[i] == 1:
            matrix[i] = 0
            break
    return numpy.asmatrix(matrix)

def encode(bits):
    G = numpy.matrix('''
        1 0 0 0 0 1 1;
        0 1 0 0 1 0 1;
        0 0 1 0 1 1 0;
        0 0 0 1 1 1 1
    ''')
    x = numpy.matrix(bits)
    xG = x * G
    xG = binary_matrix(xG)
    return xG

def decode(xG):
    H = numpy.matrix('''
        0 0 0 1 1 1 1;
        0 1 1 0 0 1 1;
        1 0 1 0 1 0 1
    ''')
    Hy = H * xG.T
    Hy = binary_matrix(Hy)

    if sum(Hy) != 0:
        # when an error occured try to correct it
        biterror = get_biterror(Hy)
        xG = recover_correct_code(xG, biterror)
        error = True
    else:
        error = False
    return xG, error

def put_errors(matrix):
    for element in numpy.nditer(matrix, op_flags=['readwrite']):
        if random.random() < 0.1:
            if element == 0:
                element[...] = 1
            else:
                element[...] = 0
    return matrix

def channel(bits):
    # create the hamming code
    hamming_code = encode(bits)
    # create random errors
    transmitted = put_errors(hamming_code)
    # try to decode
    received, error = decode(transmitted)

    if (hamming_code == received).all():
        return (True, error)
    else:
        return (False, error)

def create_single_block():
    bits = ''
    for i in range(4):
        if random.random() < 0.5:
            bits += '1 '
        else:
            bits += '0 '
    return bits

def test(num_of_tests):
    correct_counter = 0
    errors_counter = 0
    for i in range(num_of_tests):
        bits = create_single_block()
        response, error = channel(bits)
        if response == True:
            correct_counter += 1
        if error == True:
            errors_counter += 1
    print 'Tests:', num_of_tests
    print 'Errors:', errors_counter
    print 'Corrects:', correct_counter

def main():
    if len(sys.argv) > 1:
        num_of_tests = int(sys.argv[1])
        test(num_of_tests)
    else:
        print 'Missing parameters'

if __name__ == '__main__':
    main()

