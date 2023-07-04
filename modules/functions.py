FILEPATH = "todos.txt"


def get_todos(file_path=FILEPATH):
    """
    Reads todos from a file and returns an array of todos
    """
    with open(file_path, 'r') as file:
        return file.readlines()


def save_todos(todos_list, file_path=FILEPATH):
    with open(file_path, 'w') as file:
        file.writelines(todos_list)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
