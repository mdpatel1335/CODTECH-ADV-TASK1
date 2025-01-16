import pyfiglet
from termcolor import colored
import hashlib
import os
import time

OWNER_NAME = "Mihir Patel"
TOOL_NAME = "FILE INTEGRITY CHECKER"

def display_tool_name_and_owner():
    # Use pyfiglet to generate the tool name in ASCII art
    fig = pyfiglet.Figlet(font='slant')
    tool_name_ascii = fig.renderText(TOOL_NAME)
    
    # ANSI escape codes for bold and color formatting
    bold_owner_name = colored(OWNER_NAME, 'yellow', attrs=['bold'])
    
    # Print the tool name (ASCII art) and owner name in bold and color
    print(colored(tool_name_ascii, 'cyan'))
    print(f"Owner: {bold_owner_name}\n")
    
def display_message(message, color='white'):
    """Helper function to display messages in a color."""
    print(colored(message, color))

# Function to calculate the hash of a file using SHA-256
def calculate_file_hash(file_path, hash_algorithm='sha256'):
    """Calculate the hash of a file using the specified hash algorithm."""
    hash_func = hashlib.new(hash_algorithm)
    
    # Open file in binary mode
    with open(file_path, 'rb') as f:
        # Read the file in chunks to avoid memory overload with large files
        while chunk := f.read(4096):  # 4KB chunks
            hash_func.update(chunk)
    
    # Return the hexadecimal digest of the hash
    return hash_func.hexdigest()

# Function to load previous hash history from a file
def load_history(history_file):
    """Load the history of file hashes from the given file."""
    if not os.path.exists(history_file):
        return []  # Return empty history if no file exists
    
    with open(history_file, 'r') as file:
        history = []
        for line in file:
            try:
                timestamp, file_hash = line.strip().split(' ', 1)
                history.append((float(timestamp), file_hash))
            except ValueError:
                # Handle case where the line is not formatted correctly
                display_message(f"Warning: Skipping invalid line in history file: {line.strip()}", 'yellow')
    return history

# Function to save new hash history to a file
def save_history(history_file, history):
    """Save the history of file hashes to the given file."""
    with open(history_file, 'w') as file:
        for timestamp, file_hash in history:
            file.write(f"{timestamp} {file_hash}\n")

# Function to monitor file integrity
def monitor_file(file_path, history_file='hash_history.txt', hash_algorithm='sha256', interval=10):
    """Monitor the file for any changes by comparing hashes at regular intervals."""
    # Check if the file exists
    if not os.path.isfile(file_path):
        display_message(f"Error: {file_path} does not exist.", color='red')
        return
    
    # Load the previous hash history
    history = load_history(history_file)
    
    # Calculate the current hash of the file
    current_hash = calculate_file_hash(file_path, hash_algorithm)
    
    # Print the initial hash (if there is no history)
    if not history:
        display_message(f"Initial hash of {file_path}: {current_hash}", color='green')
    
    # If the file has been seen before, print its history
    if history:
        display_message(f"Previous file modifications:", color='yellow')
        for timestamp, file_hash in history:
            print(f"At {time.ctime(timestamp)} -> Hash: {file_hash}")

    # Add the current hash to the history (if it's not already in the history)
    if not history or current_hash != history[-1][1]:
        timestamp = time.time()
        history.append((timestamp, current_hash))
        display_message(f"\nFile {file_path} has been modified!", color='red')
        print(f"New hash: {current_hash}")
        
        # Save the updated history to the file
        save_history(history_file, history)
    
    # Monitor the file at regular intervals
    try:
        while True:
            # Wait for the specified interval (in seconds)
            time.sleep(interval)
            
            # Calculate the current hash of the file again
            current_hash = calculate_file_hash(file_path, hash_algorithm)
            
            # Compare the current hash with the last recorded hash
            if current_hash != history[-1][1]:
                # File has been modified, record the change
                timestamp = time.time()
                history.append((timestamp, current_hash))
                
                display_message(f"\nFile {file_path} has been modified!", color='red')
                print(f"New hash: {current_hash}")
                
                # Print all historical changes
                display_message("\n--- History of Changes ---", color='yellow')
                if history:
                    for timestamp, file_hash in history:
                        print(f"At {time.ctime(timestamp)} -> Hash: {file_hash}")
                else:
                    display_message("No history available.", color='cyan')
                
                # Save the updated history to the file
                save_history(history_file, history)
            else:
                display_message(f"File {file_path} is unchanged.", color='green')
    
    except KeyboardInterrupt:
        display_message("\nMonitoring stopped by user.", color='cyan')
        # Print the full history of changes when stopping the monitoring
        display_message("\n--- Full History of Changes ---", color='yellow')
        for timestamp, file_hash in history:
            print(f"At {time.ctime(timestamp)} -> Hash: {file_hash}")

# Main function to run the monitoring
if __name__ == "__main__":
    display_tool_name_and_owner()
    file_path = input(colored("Enter the path of the file to monitor: ", 'cyan'))
    monitor_file(file_path)

#
