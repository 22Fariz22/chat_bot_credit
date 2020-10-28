# -*- coding: utf-8 -*-
import json
import os

def write_json(person_dict):
    try:
        with open('persons.json') as f:
            data = json.load(f)
    except:
        data = []

    data.append(person_dict)

    with open('persons.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

    


