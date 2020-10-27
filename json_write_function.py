# -*- coding: utf-8 -*-
import json
import os

def write_json(person_dict):
    try:
        json.load(open('person.json'))
    except:
        data = []

    data.append(person_dict)

    with open('persons.json', 'a', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
        file.write(os.linesep)

    # with open('persons.json', encoding='utf-8') as file:
    #     json.dump(data, file, indent=2, ensure_ascii=False)

    # with open('persons.json', 'a') as file:
    #     json.dump(data, file, indent=2, ensure_ascii=False)
    # with open('person_dict.json', 'a', encoding='utf-8') as file:
    #     json.dump(person_dict, file, ensure_ascii=False)


