def get_tasklist(filepath="tasks.txt"):
    """Retrieve the tasklist from the textfile to prepare it for modification"""
    with open(filepath, 'r') as file_local:
        tasks_local = file_local.readlines()
    return tasks_local


def write_tasklist(your_list, filepath="tasks.txt"):
    """Overwrites the tasklist with a new list"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(your_list)
