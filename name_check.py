import subprocess


class NameCheck:

    def __init__(self, name, surname):
        try:
            powershell_script_path = "script.ps1"

            command = [
                "powershell.exe",
                "-File", powershell_script_path,
                "-name", name,
                "-surname", surname
            ]

            result = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = result.communicate()
            print(stdout)

            # Check for any errors
            if result.returncode != 0:
                print("PowerShell script encountered an error.")
                print(stderr)

        except Exception as e:
            print(f"Error occurred: {e}")