import pandas as pd
from new_hire import NewHire
from conversion import Conversion
import os

path = input("Enter path: ")
data_file = pd.read_csv(path.strip('"'))
data_file.insert(loc=22, column="REQ NUMBER", value="")

file_length = len(data_file.index)
i = 0
while i < file_length:
    hire_reason = data_file["HIRE REASON"][i]
    if hire_reason == "New Hire":
        new_hire = NewHire(data_file, i)
        new_hire.show_records()
        new_hire.copy_to_clipboard()
        req_number = input("Paste in ready REQ number: ")
        row_index = data_file.index[i]
        data_file.loc[row_index, "REQ NUMBER"] = req_number
    elif hire_reason == "Convert to Employee":
        conversion = Conversion(data_file, i)
        conversion.show_records()
        conversion.copy_to_clipboard()
        req_number = input("Paste in ready REQ number: ")
        row_index = data_file.index[i]
        data_file.loc[row_index, "REQ NUMBER"] = req_number
    elif hire_reason == "Rehire":
        new_hire = NewHire(data_file, i)
        new_hire.show_records()
        new_hire.copy_to_clipboard()
        new_hire.rehire()
        req_number = input("Paste in ready REQ number: ")
        row_index = data_file.index[i]
        data_file.loc[row_index, "REQ NUMBER"] = req_number
    i += 1

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
data_file.to_csv(path_or_buf=path.strip('"'), index=False)
