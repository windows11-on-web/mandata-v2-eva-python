# Modules First
import ping3
import random
import socket
import string
import os
import shutil
import time

# This uses the Lilyhosting API ping to make a user data request, Used for Lilyhositng to look users who are using this tool

response_time = ping3.ping('28.128.121.129')
if response_time is not None:
    print(f"Response time: 10 ms")
else:
    print("Response time: 100 ms")

# Print that the database is starting
    
print("The Database has been started")
print("Mandata | v2 EVA | Made By Katy")

def create_database():
    # Get the root folder where the code is located
    root_folder = os.path.dirname(os.path.abspath(__file__))
    
    # Create the "database-local" folder if it doesn't exist
    database_folder = os.path.join(root_folder, "database-local")
    if not os.path.exists(database_folder):
        os.makedirs(database_folder)
        print(f"Created 'database-local' folder at root")
    
    # Loop indefinitely
    while True:
        # Get a list of all files in the root folder
        files = [f for f in os.listdir(root_folder) if os.path.isfile(os.path.join(root_folder, f))]
        
        # Iterate over the files and copy/move them to the "database-local" folder
        for file in files:
            if file != os.path.basename(__file__):  # Exclude the current script file
                file_path = os.path.join(root_folder, file)
                destination_path = os.path.join(database_folder, file)
                shutil.copy(file_path, destination_path)  # Change to shutil.move if you want to move instead of copy
                print(f"File Request has been accepted")
        
        # Wait for a specified interval before checking for new files again (e.g., every 3 seconds by default)
        time.sleep(3)

# Call the function to start creating the database
create_database()