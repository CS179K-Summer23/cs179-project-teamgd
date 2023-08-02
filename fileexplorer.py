import os

def loaddirectory():
    # Base directory. Change path to respective folder
    dir_path = os.getcwd()

    # dict for files
    storage = []

    # Iterate directory
    for file_path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, file_path)):
            storage.append(file_path)
    print(storage)

loaddirectory()