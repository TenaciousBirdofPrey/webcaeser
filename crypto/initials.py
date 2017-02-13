def get_initials(fullname):
    """ Given a person's name, return the person's initials (uppercase) """
    # TODO your code here

    up_fullname = fullname.upper()
    split_name = up_fullname.split()
    # print(split_name)
    initial_list = []
    for e in split_name:
        initial_list.append(e[0])
    return "".join(initial_list)




def main():
    person = input('Enter your name: ')
    print(get_initials(person))



if __name__ == '__main__':
    main()
