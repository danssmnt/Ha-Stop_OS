"""
Used to open .txt files in the system.
"""

from errors.system_error import *

def read_file(file):
    print("\n\n\nText:")
    with open(file, "r") as file_read:
        print(f"\"{file_read.read()}\"")
            
            
def write_file(file):
    enter_count = 0
    line_count = 0
    with open(file, "a") as file_write:
        while enter_count < 3:
            line_count += 1
            wrt_line_usr = input(f"Line {line_count}: ")
            if wrt_line_usr == "": enter_count += 1
            else: enter_count = 0; file_write.write(f"\n{wrt_line_usr}")


def append_file(file):
    enter_count = 0
    with open(file, "r") as file_temp:
        list_file = file_temp.readlines() 
    line_count = len(list_file)
    #print(f"Line {line_count}")
    with open(file, "a") as file_append:
        while enter_count < 3:
            line_count += 1
            wrt_line_usr = input(f"Line {line_count}: ")
            if wrt_line_usr == "": enter_count += 1
            else: enter_count = 0; file_append.write(f"\n{wrt_line_usr}")
        

def open_file(file):
    argv_user = input("(R)ead, (W)rite or (A)ppend? ")
    if argv_user.strip().lower() == "r": read_file(file)
    elif argv_user.strip().lower() == "w": write_file(file)
    elif argv_user.strip().lower() == "a": append_file(file)
    elif argv_user == "" or argv_user.isspace(): ArgvNotFound().show_warning(); read_file(file)
    else: ArgvNotIdentified(argv_user).show_warning(); read_file(file)
    

if __name__ == "__main__":
    print("Don't open this application from main!\nRun it trough your system.")
    