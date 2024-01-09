
import os
import os.path

# get the current working directory
current_working_directory = os.getcwd()

# print output to the console
print(current_working_directory)

path=current_working_directory+"/new5.pdf"


check_file = os.path.isfile(path)

print(check_file)
