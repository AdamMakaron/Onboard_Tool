import pyperclip
import time
import datetime


class Conversion:

    def __init__(self, data_file, i):
        self.username = data_file["FULL NAME"][i]
        self.emp_num = str(data_file["EMPLOYEE NUMBER"][i])
        self.user_id = data_file["USER ID"][i]
        self.hire_date = data_file["HIRE DATE"][i]
        self.hire_date = self.hire_date[:-6]
        self.manager_email = data_file["MANAGER EMAIL ADDRESS"][i]
        self.location = data_file["PERSONNEL SUBAREA TEXT"][i]

    def show_records(self):
        print("Conversion detected!")
        print(f"Requested for {self.manager_email}")
        print(f"User conversion request for [{self.username}] [{self.user_id}] empl id [{self.emp_num}] / HIRE DATE [{self.hire_date}]")

    def copy_to_clipboard(self):
        pyperclip.copy(self.hire_date)
        time.sleep(3)
        pyperclip.copy(self.location)
        time.sleep(3)
        pyperclip.copy(self.emp_num)
        time.sleep(3)
        pyperclip.copy(self.user_id)
        time.sleep(3)
        pyperclip.copy(self.username)
        time.sleep(3)
        pyperclip.copy(f"User conversion request for [{self.username}] [{self.user_id}] empl id [{self.emp_num}] / HIRE DATE [{self.hire_date}]")
        time.sleep(3)
        pyperclip.copy(self.manager_email)
        time.sleep(3)

        if self.location[0:3] == "JPN":
            new_hire_date = datetime.datetime(int(self.hire_date[0:4]), int(self.hire_date[5:7]), int(self.hire_date[8:10]))
            new_hire_date = new_hire_date - datetime.timedelta(days=10)
            self.hire_date = str(new_hire_date)
            self.hire_date = self.hire_date[0:10]
            print(
                f"It is Japanese user! Remember to tag it with a proper Hire Date [{new_hire_date}]! It has been copied to your Clipboard! ")
        pyperclip.copy(self.hire_date)
