text = 'aababaabababbaabababababaabbababababaabbababbababba'
p = 'abba'
counter = 0
for i in range(len(text)):
    part = ''
    try:
        part = text[i] + text[i+1] + text[i+2] + text[i+3]
        if p == part:
            print i
            counter += 1
    except:
        pass

print counter
