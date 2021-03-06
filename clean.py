import os
from shutil import move, rmtree


def get_author(folder_name):
    author = ""
    flag = False
    for char in folder_name:
        if char == '[':
            flag = True
        elif char == ']':
            flag = False
        if flag:
            author += char
    if author:
        return author[1:]


def clean_up(TARGET_PATH, GOAL_PATH):
    folder_list = os.listdir(TARGET_PATH)
    for folder in folder_list:
        author = get_author(folder)
        if author:
            print(f"Moving {folder} ...")
            if not os.path.isdir(f"{GOAL_PATH}\\{author}"):
                os.mkdir(f"{GOAL_PATH}\\{author}")
            if not os.path.isdir(f"{GOAL_PATH}\\{author}\\{folder}"):
                move(f"{TARGET_PATH}\\{folder}",
                     f"{GOAL_PATH}\\{author}\\{folder}")
            else:
                rmtree(f"{TARGET_PATH}\\{folder}")
    print("Done")
