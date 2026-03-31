import json

def load_skill_dictionary():

    with open("data/master_skill_dictionary.json") as f:
        skill_db = json.load(f)

    return skill_db


def load_skill_stacks():

    with open("data/skill_stacks.json") as f:
        stack_db = json.load(f)

    return stack_db