from new_users_class import *

user_list = []
# open_and_print('names.txt')

try:
    with open('names.txt', 'r') as file:
        lines_list = file.readlines()
        for line in lines_list:
            print(line.rstrip('\n').title())
            user = New_users(line.rstrip('\n'))
            user_list.append(user)

except FileNotFoundError as err:
    print('check your file')
    print(err)
finally:
    print('-----Text file Read----')

user_list[3].user_info()




# create_object('names.txt')