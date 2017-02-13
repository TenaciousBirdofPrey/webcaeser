from helpers import alphabet_position, rotate_character
from sys import argv

def user_input_is_valid(argv):
    if len(argv)<2 or len(argv)>2:
        #print("usage")
        return False
    it =argv[1]
    if it.isdigit()==True:

        return True
    else:
        #print("must enter number")
        return False




def encrypt(str, num):
    code = []
    for e in str:
        if e.isalpha():
            code.append(rotate_character(e,num))
        else:
            code.append(e)
    return "".join(code)


def main():
    if user_input_is_valid(argv) == False:
        exit()
    get_string = input("Type a message")
    print (      encrypt(get_string,int(argv[1])     )         )

if __name__ == '__main__': # don't worry about how this works, just copy it
    main()