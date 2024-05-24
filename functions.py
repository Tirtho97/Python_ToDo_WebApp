def get_todos(filepath='todos.txt'):
    """
    Reads a text file and returns the list of to-do items.
    """
    with open(filepath, 'r') as file_get:
        todos_local = file_get.readlines()
    return todos_local


def write_todos(todos_arg, filepath='todos.txt'):
    """
    Takes a to-do list as argument and writes in the text file.
    """
    with open(filepath, 'w') as file_write:
        file_write.writelines(todos_arg)


if __name__ == "__cli__":
    print("Hello")
    print(get_todos())