#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import yaml

from classes import *


def load_data(file):
    persons = {}
    units = []

    with open(file, newline = '', encoding = 'utf-8') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
        for item in yaml_data:

            husband_name = item['husband']
            if husband_name not in persons:
                persons[husband_name] = Person(husband_name, is_male = True)
            husband = persons[husband_name]

            wifes = []
            for wife_name in item.get('wifes', []):
                if wife_name not in persons:
                    persons[wife_name] = Person(wife_name, is_male = True)

            concubines = []
            for concubine_name in item.get('concubines', []):
                if concubine_name not in persons:
                    persons[concubine_name] = Person(concubine_name, is_male = True)

            children = []
            for child in item.get('children', []):
                child_name = child['name']
                child_is_male = child['sex'] == '男'
                child_father = husband

                child_mother_name = child['mother'] if 'mother' in child else None
                child_mother = persons[child_mother_name] if child_mother_name in persons else None
                if child_mother is None and wifes:
                    child_mother = wifes[0]

                persons[child_name] = Person(child_name, child_is_male, child_father, child_mother)

            unit = Unit(-1, husband, wifes, concubines, children)
            units.append(unit)

    return persons, units


def viz_graphic(units):
    pass


if __name__ == "__main__":
    persons, units = load_data('红楼梦.yaml')
