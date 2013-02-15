import sys, random

def bit_generator(zero_freq):
    if random.uniform(0, 1) < zero_freq:
        return '0'
    else:
        return '1'

def word_generator(word_length, zero_freq):
    word = ''
    for i in range(word_length):
        word = word + bit_generator(zero_freq)
    return word

def transmitter(word, word_length, zeros_occur, ones_occur):
    sended = ''
    for i in range(word_length):
        if word[i] == '0':
            if random.random() < zeros_occur:
                sended += '0'
            else:
                sended += '1'
        else:
            if random.random() < ones_occur:
                sended += '1'
            else:
                sended += '0'
    return sended

def simulation(word_length, repetitions, zero_freq, zeros_occur, ones_occur):
    word = word_generator(word_length, zero_freq)
    counter = 0.0
    for i in range(repetitions):
        sended = transmitter(word, word_length, zeros_occur, ones_occur)
        if word == sended:
            counter += 1
    porcentage = counter/repetitions
    print '%.2f' % porcentage

def main():
    if len(sys.argv) > 5:
        word_length = int(sys.argv[1])
        repetitions = int(sys.argv[2])
        zero_freq = float(sys.argv[3])
        zeros_occur = float(sys.argv[4])
        ones_occur = float(sys.argv[5])
        simulation(word_length, repetitions, zero_freq, zeros_occur, ones_occur)
    else:
        print 'Missing parameters'

if __name__ == '__main__':
    main()

