# def check_names():
#     with open("names.txt", "r", encoding="UTF-8") as file:
#         file = file.read().split()
#         correct_names = []
#
#         for elem in file:
#             names_str = ""
#             for symbols in elem:
#                 if symbols.isalpha():
#                     names_str += symbols
#             if names_str.isalpha():
#                 correct_names.append(names_str)
#
#
#
#
#     return "\n".join(correct_names)
#
#
# print(check_names())

import re

def check_names():
    with open("names.txt", "r", encoding="UTF-8") as f:
        content = f.read().split()

    file_list = []

    for elem in content:
        words = re.findall(r"[A-Za-zА-Яа-я]+", elem)
        if words:
            file_list.extend(words)


    return "\n".join(file_list)


print(check_names())
