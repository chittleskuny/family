#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Person:
    def __init__(self, name, is_male, father, mother):
        self.name = name
        self.is_male = is_male
        self.father = father
        self.mother = mother

        if self.father is not None:
            self.rank = self.father.rank + 1
        elif self.mother is not None:
            self.rank = self.mother.rank + 1
        else:
            self.rank = 0

    def greet(self):
        return f"Hello, my name is {self.name}."


class Household:
    def __init__(self, husband, wife, concubines):
        self.husband = husband
        self.wife = wife
        self.concubines = concubines

        self.rank = self.husband.rank
