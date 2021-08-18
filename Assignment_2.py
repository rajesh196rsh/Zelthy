import os
from datetime import date, datetime

# to get the current date
today = date.today()
dir_name = today.strftime("%d-%m-%Y")

# to check if the directory exist or need to be created
if not (os.path.isdir(f'./{dir_name}')):
    os.mkdir(f'./{dir_name}')

# to get the user input and save it to a text file
user_input = input("Please enter file contents?")
file_name = f'file_{datetime.now().strftime("%H-%M-%S")}.txt'
file_path = f'./{dir_name}/{file_name}'
f = open(file_path, 'w+')
f.write(user_input)
f.close()