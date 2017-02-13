from helpers import alphabet_position, rotate_character


def encrypt(str, key):
    key_list = []
    key_len = len(key)
    vig = 0
    for e in key:
        key_list.append(alphabet_position(e))

    code = []
    for e in str:
        if e.isalpha():

            vig_counter = vig % key_len
            code.append(rotate_character(e, key_list[vig_counter]))
            vig = vig + 1
        else:
            code.append(e)
    return "".join(code)

def main():
    get_string = input("Type a message")
    get_key = input("Enter Key:")
    print (      encrypt(get_string,get_key)     )


if __name__ == '__main__':
    main()
