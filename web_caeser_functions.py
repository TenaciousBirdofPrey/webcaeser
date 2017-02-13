def alphabet_position(letter):
    if letter.isupper():
        return ord(letter)-65
    else:
        return ord(letter)-97

def rotate_character(char, rot):
    pos = alphabet_position(char)
    shift = rot%26
    key = pos +shift
    if key > 25:
        key = key%26
    if char.isupper():
        return (chr(65+key))
    else:
        return (chr(97+key))


def encrypt(str, num):
    code = []
    for e in str:
        if e.isalpha():
            code.append(rotate_character(e,num))
        else:
            code.append(e)
    return "".join(code)