from new_users_class import *
from functions import *





open_print('names.txt')

choose_user = int(input('Which user to you want to use')) - 1
user_list[choose_user].user_info()


# while True:
#
#     option = input('What would you like to do?\n 1.Print Text File \n 2.Create new user file\n')
#     if option == '1':
#         open_print('names.txt')
#
#     elif option == '2':
#         # choose_user = int(input('Which user to you want to use')) - 1
#         # user_list[choose_user].user_info()
#         print(user_list)
#     else:
#         print('Enter 1 or 2 please')



