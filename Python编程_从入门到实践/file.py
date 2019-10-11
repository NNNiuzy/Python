# with open("./pi_digits.txt") as file_object:
#     # contents = file_object.read()
#     # print(contents.rstrip())
#
#     # for line in file_object:
#     #     print(line.rstrip())
#
#     lines = file_object.readlines()
# for line in lines:
#     print(line.rstrip())

# filename = 'pi_million_digits.txt'

# filename = 'programming.txt'
# with open(filename,'a') as file_object:
#     #     lines = file_object.readlines()
#     #
#     # pi_string = ''
#     # for line in lines:
#     #     pi_string += line.strip()
#     # #
#     # # print(pi_string[:52]+"...")
#     # # print(len(pi_string))
#     # birthday = input("Enter your birthday, in the form mmddyy: ")
#     # if birthday in pi_string:
#     #     print("yes")
#     # else:
#     #     print("no")
#     file_object.write("text\n")
#
# filename = 'alice.txt'
# try:
#     with open(filename, 'rb') as file_object:
#         contents = file_object.read()
# except FileNotFoundError:
#     print("Sorry, the file " + filename + " does mpt exit.")
# else:
#     words = contents.split()
#     num_words = len(words)
#     print(num_words)

import json

# numbers = [2, 3, 4, 5, 6, 7, 8]
# filename = 'number.json'
# with open(filename, 'w') as f_obj:
#     json.dump(numbers, f_obj)

# username = input("What is your name: ")
filename = 'username.json'
# with open(filename,'a') as f_obj:
#     json.dump(username,f_obj)
with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back " + username + "!")

