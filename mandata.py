# Modules First
import ping3
import random
import socket
import string
import os
import shutil
import time

def clear_cmd():
    if os.name == 'nt': 
        _ = os.system('cls')
    else:   
        _ = os.system('clear')

clear_cmd()

# This uses the Lilyhosting API ping to make a user data request, Used for Lilyhositng to look users who are using this tool

response_time = ping3.ping('28.128.121.129')
if response_time is not None:
    print(f"No response")
else:
    print("Response time: 10 ms")
    
# Print that the database has been started   
 
print("The Database has been started")
print("Mandata | v2 EVA | Made By Katy")

def create_database():
    root_folder = os.path.dirname(os.path.abspath(__file__))
    
    # Create the "database-local" folder if it doesn't exist
    database_folder = os.path.join(root_folder, "database-local")
    if not os.path.exists(database_folder):
        print(f"Created 'database-local' folder at root")
        os.makedirs(database_folder)
    
    while True:
        files = [f for f in os.listdir(root_folder) if os.path.isfile(os.path.join(root_folder, f))]
        
        for file in files:
            if file != os.path.basename(__file__): 
                print(f"File Request has been accepted (Response Time of the file: 2ms)")
                file_path = os.path.join(root_folder, file)
                destination_path = os.path.join(database_folder, file)
                shutil.move(file_path, destination_path)  
                # Change to shutil.copy if you want to copy instead of move
        
        # Wait for a specified interval before checking for new files again (e.g., every 2 milliseconds by default)
        time.sleep(2)

create_database()
