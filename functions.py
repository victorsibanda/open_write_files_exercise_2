from new_users_class import *
user_list=[]
def open_print(filename):
    try:
        with open(filename, 'r') as file:
            lines_list = file.readlines()
            count = 1
            for line in lines_list:
                print(count, '-', line.rstrip('\n').title())
                user = New_users(line.rstrip('\n'))
                user_list.append(user)
                count += 1

    except FileNotFoundError as err:
        print('check your file')
        print(err)
    finally:
        print('-----Text file Read----')