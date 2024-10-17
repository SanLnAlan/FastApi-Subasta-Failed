import json

def read_users():
    with open("data/users.json") as file:
        users = json.load(file)
    return users

def read_user(id: int):
    with open("data/users.json") as file:
        users = json.load(file)
    id = f'{id}'
    return users[id]
