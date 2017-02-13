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