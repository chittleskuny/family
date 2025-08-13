#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import sys

from person import *


def load_csv(file):
    family = {}
    with open(file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        is_header = True

        for row in reader:
            if is_header:
                is_header = False
                continue

            if len(row) == 4:
                name, sex, father, mother = row
                is_male = sex == '男'

                if father:
                    if father in family:
                        father = family[father]
                    else:
                        father = Person(father, True, None, None)
                else:
                    father = None
                if mother:
                    if mother in family:
                        mother = family[mother]
                    else:
                        mother = Person(mother, False, None, None)
                else:
                    mother = None

                person = Person(name, is_male, father, mother)
                family[name] = person

    return family


def viz_graphic(family):
    for name, person in family.items():
        print(f"Name: {name}, Sex: {'Male' if person.is_male else 'Female'}, Father: {person.father.name if person.father else 'Unknown'}, Mother: {person.mother.name if person.mother else 'Unknown'}")


if __name__ == "__main__":
    family = load_csv('红楼梦.csv')
    viz_graphic(family)
