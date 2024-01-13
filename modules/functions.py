# realtive to location of this file
import os
data_folder = os.path.dirname(os.path.realpath(__file__))
data_file = data_folder + '/../data/todos.txt'


def get_todos(file=data_file):
    """ Read a text file and return rows in that file as a list."""
    with open(file, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_local, file=data_file):
    """ Write the items in the array passed as todos to a file as lines."""
    with open(file, 'w') as file:
        file.writelines(todos_local)

def show_todos(todos_local=[]):
    if not todos_local:
        todos_local = get_todos()
    for index, item in enumerate(todos_local):
        item = item.strip('\n')  # shortest way to strip newlines
        print ( f"{index + 1} - {item.capitalize()}")

if __name__ == "__main__":
    print ("hello from functions\n")
    print (get_todos() )
    print ("\n")
    print (__name__)
    print (__path__)