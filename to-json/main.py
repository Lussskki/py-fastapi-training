import os
import json

def add_task(name):  
    db_folder = "db1"
    task = [{"Name: ": name}]
    tasks_file = os.path.join(db_folder, "database.json")

    if not os.path.exists(tasks_file):
        with open(tasks_file, 'w', encoding='utf-8') as file:
            json.dump([], file)

    try:
        with open(tasks_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        data = []

    if data != {}:
        data.append({"Name": name})
        print("Succesfuly added your name")
    else:
        print("ERROR")    

    with open(tasks_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    name = input("What is your name? ")
    add_task(name)

# update existing data into json