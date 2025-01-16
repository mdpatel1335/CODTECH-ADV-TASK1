# CODTECH-ADV-TASK1
# Personal Information:
- NAME: Patel Mihir

- COMPANY: CODTECH IT SOLUTIONS 

- ID: CT08DAB

- DOMAIN: Cyber Security & Ethical Hacking

- DURATION: 20th dec 2024 to 20th jan 2025

- MENTOR:Neela Santhosh Kumar





# OVERVIEW OF THE PROJECT:
# File Integrity Checker

This is a Python tool for monitoring the integrity of files by calculating their hash and comparing the current hash with the previous ones to detect any modifications. It uses the SHA-256 hashing algorithm (or others as specified) to ensure that the file remains unaltered over time. If any modification is detected, it alerts the user with the new file hash and records the timestamp of the change.


# Features:

- File Integrity Monitoring: Monitors files for modifications by calculating and comparing file hashes (SHA-256 by default).
- Historical Hash Records: Keeps track of previous file hashes and timestamps, allowing you to see when changes occurred.
- Real-Time Alerts: Alerts the user when the file is modified, displaying the new hash and the change history.
- Customizable Hash Algorithm: The hash algorithm can be changed to other supported algorithms such as md5, sha512, etc.
- File History Storage: Stores the file's hash history in a text file (hash_history.txt).
- Regular Monitoring: Automatically checks for modifications at user-defined intervals.
- Graceful Exit: Allows the user to stop the monitoring at any time and shows a full history of changes.

# Requirements:
The following Python libraries are required to run this tool:

- pyfiglet: For generating ASCII art of the tool name.
- termcolor: For adding color to terminal output.
- hashlib: For hashing files using SHA-256 or other algorithms.
- os: For file and directory handling.
- time: For monitoring intervals and timestamps.

<br>
You can install the required dependencies using pip:

    pip install pyfiglet termcolor

hashlib, os, and time are part of the standard Python library, so no additional installation is needed for them.

# Run Steps:
- Clone the Repository or Download the Script:

You can clone this repository or simply download the script file to your local system.

    git clone https://github.com/yourusername/file-integrity-checker.git
    cd file-integrity-checker

- Run the Script:

Make sure you have Python 3.x installed on your system. Then, run the Python script using the following command:

    python file_integrity_checker.py

- Input the File to Monitor:

When prompted, enter the path of the file you want to monitor for changes. The tool will then start monitoring the file.

- Monitor the File:

The tool will continuously monitor the file and alert you whenever the file's hash changes (indicating a modification). The monitoring will continue until you stop it by pressing Ctrl + C.

- View the Change History:

The script saves a history of changes (if any) in a file named hash_history.txt. You can view the full history of changes at any time by stopping the monitoring, and the script will display all the previous hashes and timestamps.



# Options

- File Path: The path of the file to monitor for integrity.
- Hash Algorithm: The hashing algorithm to use (default is sha256).
- Interval: The interval (in seconds) between each file hash check (default is 10 seconds).
- History File: The file where the hash history is stored (default is hash_history.txt).

# File Integrity Checking Flow

- Initial Check: The tool calculates the hash of the file when it is first monitored and displays it.
- File Modification Detection: The tool continuously checks the file's hash at regular intervals (e.g., every 10 seconds).
- Alert on Modification: If the file's hash changes, it records the new hash and alerts the user.
- History Recording: All file changes (hash updates) are saved in the hash_history.txt file for future reference.


# screenshots

![Screenshot From 2025-01-16 14-12-57](https://github.com/user-attachments/assets/58b4ccb5-b7e9-4853-aecf-e99202b419c7)

![Screenshot From 2025-01-16 14-13-43](https://github.com/user-attachments/assets/0f771e90-c6fd-40de-8648-f8e024c65506)
