import pandas as pd
from new_hire import NewHire
from conversion import Conversion
import os
import itertools
from name_check import NameCheck


def generate_name_combinations(name_parts):
    name_combinations = []
    for r in range(1, len(name_parts)):
        for combination in itertools.permutations(name_parts, r):
            if combination[0] != combination[-1]:
                name_combinations.append(combination)
    name_combinations.append(name_parts)
    return name_combinations


def clear():
    os.system('cls')


path = input("Enter path: ")
data_file = pd.read_csv(path.strip('"'))
data_file.insert(loc=22, column="REQ NUMBER", value="")

file_length = len(data_file.index)
i = 0
while i < file_length:
    hire_reason = data_file["HIRE REASON"][i]
    if hire_reason == "New Hire":
        clear()
        new_hire = NewHire(data_file, i)
        new_hire.show_records()
        new_hire.copy_to_clipboard()

        name_parts = new_hire.username.split()
        name_combinations = generate_name_combinations(name_parts)
        for idx, combination in enumerate(name_combinations, start=1):
            full_name = " ".join(combination)
            print(f"{idx}. {full_name}")
            name_check = NameCheck(combination[0], combination[-1])

        req_number = input("Paste in ready REQ number: \n If you figured out that it is conversion, type: conversion \n")
        if req_number == "conversion":
            clear()
            print("You switched up to conversion! Please remember to double check user ID and employee ID!")
            print("Remember that there is not FTE to CTR conversion!")
            conversion = Conversion(data_file, i)
            conversion.show_records()
            conversion.copy_to_clipboard()

            name_parts = conversion.username.split()
            name_combinations = generate_name_combinations(name_parts)
            for idx, combination in enumerate(name_combinations, start=1):
                full_name = " ".join(combination)
                print(f"{idx}. {full_name}")
                name_check = NameCheck(combination[0], combination[-1])

            req_number = input("Paste in ready REQ number: ")
            row_index = data_file.index[i]
            data_file.loc[row_index, "REQ NUMBER"] = req_number
        else:
            row_index = data_file.index[i]
            data_file.loc[row_index, "REQ NUMBER"] = req_number
    elif hire_reason == "Convert to Employee":
        clear()
        conversion = Conversion(data_file, i)
        conversion.show_records()
        conversion.copy_to_clipboard()

        name_parts = conversion.username.split()
        name_combinations = generate_name_combinations(name_parts)
        for idx, combination in enumerate(name_combinations, start=1):
            full_name = " ".join(combination)
            print(f"{idx}. {full_name}")
            name_check = NameCheck(combination[0], combination[-1])

        req_number = input("Paste in ready REQ number: ")
        row_index = data_file.index[i]
        data_file.loc[row_index, "REQ NUMBER"] = req_number
    elif hire_reason == "Rehire":
        clear()
        new_hire = NewHire(data_file, i)
        new_hire.show_records()
        new_hire.copy_to_clipboard()
        new_hire.rehire()

        name_parts = new_hire.username.split()
        name_combinations = generate_name_combinations(name_parts)
        for idx, combination in enumerate(name_combinations, start=1):
            full_name = " ".join(combination)
            print(f"{idx}. {full_name}")
            name_check = NameCheck(combination[0], combination[-1])

        req_number = input("Paste in ready REQ number: \n If you figured out that it is conversion, type: conversion \n")
        if req_number == "conversion":
            clear()
            print("You switched up to conversion! Please remember to double check user ID and employee ID!")
            print("Remember that there is not FTE to CTR conversion!")
            conversion = Conversion(data_file, i)
            conversion.show_records()
            conversion.copy_to_clipboard()

            name_parts = conversion.username.split()
            name_combinations = generate_name_combinations(name_parts)
            for idx, combination in enumerate(name_combinations, start=1):
                full_name = " ".join(combination)
                print(f"{idx}. {full_name}")
                name_check = NameCheck(combination[0], combination[-1])

            req_number = input("Paste in ready REQ number: ")
            row_index = data_file.index[i]
            data_file.loc[row_index, "REQ NUMBER"] = req_number
        else:
            row_index = data_file.index[i]
            data_file.loc[row_index, "REQ NUMBER"] = req_number
    i += 1

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
data_file.to_csv(path_or_buf=path.strip('"'), index=False)
