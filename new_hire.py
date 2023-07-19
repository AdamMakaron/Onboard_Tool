import pyperclip
import time
import datetime
from location_check import LocationCheck


class NewHire:

    def __init__(self, data_file, i):
        self.username = data_file["FULL NAME"][i]
        self.emp_num = data_file["EMPLOYEE NUMBER"][i]
        self.user_id = data_file["USER ID"][i]
        self.hire_date = data_file["HIRE DATE"][i]
        self.hire_date = self.hire_date[:-6]
        self.manager_email = data_file["MANAGER EMAIL ADDRESS"][i]
        self.location = data_file["PERSONNEL SUBAREA TEXT"][i]

    def show_records(self):
        print(f"Requested for {self.manager_email}")
        print(f"Workday onboarding [{self.username}] [{self.user_id}] empl id [{self.emp_num}] / HIRE DATE [{self.hire_date}]")
        print(f"Workday onboarding [{self.username}] [{self.user_id}] empl id [{self.emp_num}] - Mailbox setup / HIRE DATE [{self.hire_date}] - Collaboration")
        print(f"Workday onboarding [{self.username}] [{self.user_id}] empl id [{self.emp_num}] - PC hardware request / HIRE DATE [{self.hire_date}] - Local IT")
        print(f"Users location: {self.location}")
        location_check = LocationCheck(self.location)
        print(f"Assign Local IT Task to: {location_check.oss}")

    def copy_to_clipboard(self):
        pyperclip.copy(f"Workday onboarding [{self.username}] [{self.user_id}] empl id [{self.emp_num}] - PC hardware request / HIRE DATE [{self.hire_date}] - Local IT")
        time.sleep(3)
        pyperclip.copy(f"Workday onboarding [{self.username}] [{self.user_id}] empl id [{self.emp_num}] - Mailbox setup / HIRE DATE [{self.hire_date}] - Collaboration")
        time.sleep(3)
        pyperclip.copy(f"Workday onboarding [{self.username}] [{self.user_id}] empl id [{self.emp_num}] / HIRE DATE [{self.hire_date}]")
        time.sleep(3)
        pyperclip.copy(f"Requested for {self.manager_email}")
        time.sleep(3)

        if self.location[0:3] == "JPN":
            new_hire_date = datetime.datetime(int(self.hire_date[0:4]), int(self.hire_date[5:7]), int(self.hire_date[8:10]))
            new_hire_date = new_hire_date - datetime.timedelta(days=10)
            self.hire_date = str(new_hire_date)
            self.hire_date = self.hire_date[0:10]
            print(
                f"It is Japanese user! Remember to tag it with a proper Hire Date [{new_hire_date}]! It has been copied to your Clipboard! ")
        pyperclip.copy(self.hire_date)
        time.sleep(3)

    def rehire(self):
        print("This is REHIRE! Additional task to HCL - IAM team needed!")
        print(f"REHIRE Workday onboarding [{self.username}] [{self.user_id}] empl id [{self.emp_num}] / HIRE DATE [{self.hire_date}]")
        pyperclip.copy(f"REHIRE Workday onboarding [{self.username}] [{self.user_id}] empl id [{self.emp_num}] / HIRE DATE [{self.hire_date}]")
